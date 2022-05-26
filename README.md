# streamlit-google-oauth
An example [Streamlit](https://streamlit.io/) application that incorporates Google OAuth 2.0

## PIP
```bash
pip install git+https://github.com/hunkim/streamlit-google-oauth
```

## Setup Google OAuth client ID
<img width="1434" alt="image" src="https://user-images.githubusercontent.com/901975/170391098-c3a79b40-283a-4f78-a318-c4603bb18bb9.png">


### Make sure people api is enabled
<img width="1070" alt="image" src="https://user-images.githubusercontent.com/901975/170388473-4664ce58-6a06-4237-9fbe-d88787f41c22.png">


## Put client id, etc. in env
Put in the .env file
```bash
~/streamlit-google-oauth$ cat .env 
GOOGLE_CLIENT_ID=767025784452-fscnojvddiek...
GOOGLE_CLIENT_SECRET=GOCSPX-KE4_...
GOOGLE_REDIRECT_URI=http://localhost:8080
```

or 
```bash
export GOOGLE_CLIENT_ID="xxx"
export GOOGLE_CLIENT_SECRET="yyy"
export GOOGLE_REDIRECT_URI="http://localhost:8501"
```

## Add login in your streamlit app
```python
import streamlit as st
import os
from dotenv import load_dotenv
import streamlit_google_oauth as oauth

load_dotenv()
client_id = os.environ["GOOGLE_CLIENT_ID"]
client_secret = os.environ["GOOGLE_CLIENT_SECRET"]
redirect_uri = os.environ["GOOGLE_REDIRECT_URI"]


if __name__ == "__main__":
    login_info = oauth.login(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        login_button_text="Continue with Google",
        logout_button_text="Logout",
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
## Quick demo screenshots
![Quick demo](https://user-images.githubusercontent.com/901975/170390886-004e7243-7cac-4ace-91fc-ede46ad40c5f.png)



