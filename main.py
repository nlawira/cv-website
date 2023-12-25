# Importing necessary libraries
import streamlit as st
#from streamlit_lottie import st_lottie
#import requests
import plotly.graph_objs as go
from PIL import Image
import plotly.express as px
import pandas as pd

#Home Page
def home():
    #Title
    st.title("Hello, I am Nathan! :wave:")
    
    #Header Section
    st.subheader("Summary")
    st.write("I am a Chemical & Biomolecular Engineering student at Nanyang Technological University and will graduate in June 2024. \
             My academic background equips me with strong analytical, problem-solving, and \
             critical thinking skills, while my enthusiasm and passion for data analytics, coding, and software development \
             reflects my keen interest in leveraging technologies to address and solve complex challenges!")
    st.write("Eager to apply my skills, I am actively seeking a full-time position in data analytics, coding, or software-related \
             fields where I can provide my expertise to create lasting contributions and continuously improve and grow professionally!")
    st.write("---")
    return

#Main Page
def work():
    st.title("This is the work page")
    return

def education():
    st.title("This is the education page")
    return

def cca():
    st.title("This is the CCA & VA page")
    return

def hobbies():
    st.title("This is the hobbies & personal life page")
    return

def main():
    #Default settings
    st.set_page_config(page_title="My Webpage", layout="wide")

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
    st.sidebar.write("---")

    #Main Page Selection
    page = st.sidebar.selectbox('Select Page', ["Home", "Work","Education","Co-Curricular & Voluntary Activies","Hobbies & Personal Life"], index=0)
    if page == "Home":
        home()
    if page == "Work":
        work()
    if page == "Education":
        education()
    if page == "Co-Curricular & Voluntary Activies":
        cca()
    if page == "Hobbies & Personal Life":
        hobbies()


if __name__ == "__main__":
    main()