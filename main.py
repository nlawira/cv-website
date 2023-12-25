# Importing necessary libraries
import streamlit as st
import plotly.graph_objs as go
from PIL import Image
import plotly.express as px
import pandas as pd

#Home Page
def home():
    st.title("This is a website title")
    st.header("This is a header")
    st.subheader("This is a subheader")
    st.write("These are some messages")
    return

#Main Page
def work():
    st.title("This is the work page")
    return

def education():
    st.title("This is the education page")
    return

def cca_va():
    st.title("This is the CCA & VA page")
    return

def hobbies_pl():
    st.title("This is the hobbies & personal life page")
    return

def main():
    #Sidebar
    st.sidebar.image(Image.open("Images/Personal_Photo.jpg"), use_column_width = True)
    st.sidebar.markdown("""
    <center>
        <h1>Nathan Lawira</h1>
        <p>Senior Undergraduate Student in <b>Nanyang Technological University</b></p>
        <p>Pursuing a <b>Bachelor of Engineering in Chemical & Biomolecular Engineering</b> Specializing in Intellectual Property with a Minor in Modern Languages</p>
    </center>
    """, unsafe_allow_html=True)

    #Social Media Links
    st.sidebar.markdown("""
    <div style="display: flex; justify-content: center;">
        <a href='mailto:nathanlawira@gmail.com'><img src='https://static.vecteezy.com/system/resources/previews/020/009/614/original/email-and-mail-icon-black-free-png.png' width='30' style='margin-right: 20px;'></a>
        <a href='https://www.linkedin.com/in/nathan-lawira/'><img src='https://img.icons8.com/color/48/000000/linkedin.png' width='30' style='margin-right: 20px;'></a>
        <a href='https://github.com/nlawira'><img src='https://cdn-icons-png.flaticon.com/512/25/25231.png' width='30' style='margin-right: 20px;'></a>            
        <a href='https://www.instagram.com/nlawira/'><img src='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/600px-Instagram_icon.png' width='30'></a>
    </div>
    """, unsafe_allow_html=True)

    # Rest of your Streamlit app code
    st.sidebar.markdown("""<hr>""", unsafe_allow_html=True)

    #Main Page Selection
    page = st.sidebar.selectbox('Select Page', ["Home", "Work","Education","Co-Curricular & Voluntary Activies","Hobbies & Personal Life"], index=0)
    if page == "Home":
        home()
    if page == "Work":
        work()
    if page == "Education":
        education()
    if page == "Co-Curricular & Voluntary Activies":
        cca_va()
    if page == "Hobbies & Personal Life":
        hobbies_pl()


if __name__ == "__main__":
    main()