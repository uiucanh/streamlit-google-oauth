from setuptools import setup

from streamlit_google_oauth import __version__

setup(
    name="streamlit_google_oauth",
    version=__version__,
    url="https://github.com/hunkim/streamlit-google-oauth",
    author="Sung Kim",
    author_email="hunkim@gmail.com",
    py_modules=["streamlit_google_oauth"],
    install_requires=["streamlit", "httpx-oauth", "typing-extensions"],
)
