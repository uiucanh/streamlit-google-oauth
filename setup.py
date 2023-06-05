from setuptools import setup

# from streamlit_google_oauth import __version__

setup(
    name="streamlit_google_oauth",
    version="0.1",
    url="https://github.com/hunkim/streamlit-google-oauth",
    author="Sung Kim",
    author_email="hunkim@gmail.com",
    py_modules=["streamlit_google_oauth"],
    packages=["streamlit_google_oauth"],
    install_requires=[
        "protobuf<=3.20.3",
        "streamlit",
        "httpx-oauth",
        "typing-extensions",
    ],
)
