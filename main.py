# Importing necessary libraries
import streamlit as st
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd

def home():
    st.header("Hello World")

def main():
    st.sidebar.write("I am a sidebar")
    page = st.sidebar.selectbox('Select Page', ["One", "Two"], index=0)
    if page == "One":
        home()

if __name__ == "__main__":
    main()
