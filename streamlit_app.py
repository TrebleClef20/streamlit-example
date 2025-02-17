from collections import namedtuple
import altair as alt
import math
import pandas as pd

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


import streamlit as st

def say_hello(name):
    return "Hello, " + name

name = st.text_input("Enter your name")
if st.button("Say Hello"):
    result = say_hello(name)
    st.success(result)
