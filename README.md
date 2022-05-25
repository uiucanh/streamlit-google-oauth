# streamlit-google-oauth
An example Streamlit application that incorporates Google OAuth 2.0

## PIP
pip install pip install git+https://github.com/hunkim/streamlit-google-oauth

## Setup Google OAuth client ID
<img width="649" alt="image" src="https://user-images.githubusercontent.com/901975/170381382-1e73d20b-37ea-4c39-a3c1-8934b5b402e0.png">
<img width="857" alt="image" src="https://user-images.githubusercontent.com/901975/170381419-5d5daba4-656f-4591-a5a5-fa4b0a68d38c.png">
<img width="503" alt="image" src="https://user-images.githubusercontent.com/901975/170381434-b01c6e94-64be-4cef-b25a-a28651c43cd6.png">

## Put client id, etc. in env


## Add login in your streamlit app
```python
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
        login_button_text="Login with Google", logout_button_text="Logout",
    )
    if login_info:
        user_id, user_email = login_info
        st.write(f"Welcome {user_email}")
    else:
        st.write("Please login")
```

## Run streamlit with google oauth
```bash
streamlit run app.py --server.port 8080
```
