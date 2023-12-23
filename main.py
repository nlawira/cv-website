# Importing necessary libraries
import streamlit as st
import plotly.graph_objs as go
from PIL import Image
import plotly.express as px
import pandas as pd

# Include the Montserrat font from Google Fonts
font_css_link = "https://fonts.googleapis.com/css?family=Montserrat:400,700"
font_css = f'<link rel="stylesheet" type="text/css" href="{font_css_link}">'
st.markdown(font_css, unsafe_allow_html=True)

# Apply the Montserrat font in the custom CSS
custom_font_css = """
<style>
    body {
        font-family: 'Montserrat', sans-serif;
    }
</style>
"""
st.markdown(custom_font_css, unsafe_allow_html=True)

# Custom CSS to set text alignment to center
alignment_css = """
<style>
    .centered-text {
        text-align: center;
    }
</style>
"""
st.markdown(alignment_css, unsafe_allow_html=True)

# Use the custom class to apply the alignment
st.title("Centered Title")
st.write('<p class="centered-text">This text is centered.</p>', unsafe_allow_html=True)

#Home Page
def home():
    st.title("This is a website title")
    st.header("This is a header")
    st.subheader("This is a subheader")
    st.write("These are some messages")
    return

#Main Page
def work():
    return

def main():
    #Sidebar
    st.sidebar.image(Image.open("Images/Personal_Photo.jpg"), use_column_width = True)
    st.sidebar.header('Nathan Lawira')
    st.sidebar.write("Senior Undergraduate Student in Nanyang Technological University")
    st.sidebar.write("Pursuing a Bachelor of Engineering in Chemical & Biomolecular Engineering Specializing in Intellectual Property with a Minor in Modern Languages")

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
    st.sidebar.markdown("<hr>", unsafe_allow_html=True)

    #Main Page Selection
    page = st.sidebar.selectbox('Select Page', ["Home", "Work"], index=0)
    if page == "Home":
        home()

if __name__ == "__main__":
    main()