import streamlit as st
import asyncio
from httpx_oauth.clients.google import GoogleOAuth2

__version__ = "0.1"


async def write_authorization_url(client, redirect_uri):
    authorization_url = await client.get_authorization_url(
        redirect_uri,
        scope=["profile", "email"],
        extras_params={"access_type": "offline"},
    )
    return authorization_url


async def write_access_token(client, redirect_uri, code):
    token = await client.get_access_token(code, redirect_uri)
    return token


async def get_user_info(client, token):
    user_id, user_email = await client.get_id_email(token)
    return user_id, user_email


async def revoke_token(client, token):
    return await client.revoke_token(token)


def login_button(authorization_url, button_text):
    st.write(
        f"""
    <div align="right"> <a target="_self" href="{authorization_url}">
        <button>
            {button_text}
        </button>
    </a></div>
    """,
        unsafe_allow_html=True,
    )


def logout_button(button_text):
    if st.button(button_text):
        asyncio.run(
            revoke_token(
                client=st.session_state.client,
                token=st.session_state.token["access_token"],
            )
        )
        st.session_state.user_email = None
        st.session_state.user_id = None
        st.session_state.token = None
        st.experimental_rerun()


def login(
    client_id,
    client_secret,
    redirect_uri,
    login_button_text="Continue with Google",
    logout_button_text="Logout",
):
    st.session_state.client = GoogleOAuth2(client_id, client_secret)
    authorization_url = asyncio.run(
        write_authorization_url(
            client=st.session_state.client, redirect_uri=redirect_uri
        )
    )
    if "token" not in st.session_state:
        st.session_state.token = None

    if st.session_state.token is None:
        try:
            code = st.experimental_get_query_params()["code"]
        except:
            login_button(authorization_url, login_button_text)
        else:
            # Verify token is correct:
            try:
                token = asyncio.run(
                    write_access_token(
                        client=st.session_state.client,
                        redirect_uri=redirect_uri,
                        code=code,
                    )
                )
            except:
                login_button(authorization_url, login_button_text)
            else:
                # Check if token has expired:
                if token.is_expired():
                    login_button(authorization_url, login_button_text)
                else:
                    st.session_state.token = token
                    st.session_state.user_id, st.session_state.user_email = asyncio.run(
                        get_user_info(
                            client=st.session_state.client, token=token["access_token"]
                        )
                    )
                    logout_button(button_text=logout_button_text)
                    return (st.session_state.user_id, st.session_state.user_email)
    else:
        logout_button(button_text=logout_button_text)
        return (st.session_state.user_id, st.session_state.user_email)
