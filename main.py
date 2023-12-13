# Importing necessary libraries
import streamlit as st
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd

def home():
    st.header("Hello World")

def main():
    st.sidebar.write("I am a sidebar")
    page = st.sidebar.selectbox('Select Page', ["Home", "Work"], index=0)
    if page == "Home":
        home()

if __name__ == "__main__":
    main()
