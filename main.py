# Importing necessary libraries
import streamlit as st
import plotly.graph_objs as go
from PIL import Image
import plotly.express as px
import pandas as pd

class Website():
    def home():
        #Main Page
        st.title("This is a website title")
        st.header("This is a header")
        st.subheader("This is a subheader")
        return

    def work():
        #Main Page
        return

    def main():
        #Main Page
        home()
        
        #Sidebar
        st.sidebar.header("This is a sidebar header")
        st.sidebar.image("C:\Users\nathanlawira\Personal\Images\Personal_Photo.jpg")
        st.sidebar.write("This is a sidebar")
        page = st.sidebar.selectbox('Select Page', ["Home", "Work"], index=0)
        if page == "Home":
            home()

if __name__ == "__main__":
    Website.main()