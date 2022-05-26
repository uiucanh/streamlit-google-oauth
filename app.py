import streamlit as st
import os
import asyncio
from dotenv import load_dotenv
import streamlit_google_oauth as oauth

load_dotenv()
client_id = os.environ["GOOGLE_CLIENT_ID"]
client_secret = os.environ["GOOGLE_CLIENT_SECRET"]
redirect_uri = os.environ["GOOGLE_REDIRECT_URI"]


if __name__ == "__main__":
    login_info = oauth.login(
        client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri,
        login_button_text="Continue with Google", logout_button_text="Logout",
    )
    if login_info:
        user_id, user_email = login_info
        st.write(f"Welcome {user_email}")
    else:
        st.write("Please login")
# streamlit run app.py --server.port 8080
