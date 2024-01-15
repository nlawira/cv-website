# Importing necessary libraries
import streamlit as st
from streamlit_lottie import st_lottie
import requests
import plotly.graph_objs as go
from PIL import Image
import plotly.express as px
import pandas as pd

# Initial Settings
st.set_page_config(page_title="My Webpage", layout="wide")

# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style/", unsafe_allow_html=True)

local_css("style/style.css")

# Defining Pages
def home():
    with st.container():
        # --- TITLE & SUMMARY ---
        st.title("Hello, I am Nathan! :wave:")
        st.subheader("Summary")
        st.write("I am a Chemical & Biomolecular Engineering student at Nanyang Technological University and will graduate in June 2024. \
                My academic background equips me with strong analytical, problem-solving, and \
                critical thinking skills, while my enthusiasm and passion for data analytics, coding, and software development \
                reflects my keen interest in leveraging technologies to address and solve complex challenges!")
        st.write("Eager to apply my skills, I am actively seeking a full-time position in data analytics, coding, or software-related \
                fields where I can provide my expertise to create lasting contributions and continuously improve and grow professionally!")
   
    with st.container():
        # ---
        st.write("---")
    
    with st.container():
        # --- PERSONALITY ---
        st.write("---")
        st.subheader("Personality")
        # MBTI Type and Description and Last Taken
        mbti_type = "Architect (INTJ-T)"
        mbti_description = "Architects are imaginative and strategic thinkers, with a plan for everything. \
            These thoughtful tacticians love perfecting the details of life, applying creativity and rationality. \
            They embrace rationality and impartiality, excelling in intellectual debates and scientific or technological fields. \
            They are fiercely independent, open-minded, and strong-willed."
        last_taken = "Test Taken on June 20, 2022"
        # Data & Storing it into a Dataframe
        data = {
        'Category': ['Energy', 'Energy', 'Mind', 'Mind', 'Nature', 'Nature', 'Tactics', 'Tactics', 'Identity', 'Identity'],
        'Subcategory': ['Extraverted', 'Introverted', 'Intuitive', 'Observant', 'Thinking', 'Feeling', 'Judging', 'Prospecting', 'Assertive', 'Turbulent'],
        'Values': ['13%', '87%', '66%', '34%', '57%', '43%', '65%', '35%', '49%', '51%']
        }
        df = pd.DataFrame(data)
        df['Text'] = df['Subcategory'] + '  ' + df['Values']
        category_order = ['Energy', 'Mind', 'Nature', 'Tactics', 'Identity']

        # Creating the color map
        color_map = {
            'Extraverted': '#4298b4',
            'Introverted': '#b2d7e3',
            'Intuitive': '#e4ae3a',
            'Observant': '#f4dfb0',
            'Thinking': '#33a474',
            'Feeling': '#a5e3c9',
            'Judging': '#88619a',
            'Prospecting': '#d0bfd7',
            'Assertive': '#f25e62',
            'Turbulent': '#fabfc0',
        }

        # Creating the plotly bar graph
        fig = px.bar(
            df, 
            x="Values", 
            y="Category", 
            color="Subcategory", 
            orientation='h', 
            text='Text', 
            category_orders={"Category": category_order},
            color_discrete_map = color_map,
        )
        fig.update_traces(textfont=dict(size=15))
        fig.update_layout(
            title = "",
            modebar_remove=['lasso', 'select','toimage', 'pan'],
            title_font=dict(size=20),
            hovermode=False, 
            xaxis_visible=False, 
            yaxis_visible=False, 
            showlegend=False,
            margin=dict(t=5, b=5),)
        
        # Display everything
        st.subheader(mbti_type)
        st.write(mbti_description)
        st.plotly_chart(fig, use_container_width=True)
        st.write(last_taken)
    
    with st.container():
        # --- CONTACT ME ---
        st.write("---")
        st.subheader("Get in Touch with Me!")
        contact_form = """
        <form action="https://formsubmit.co/nathanlawira@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="message" placeholder="Your Message Here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
    return

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
    with st.container():
        # Sidebar Image and Description
        st.sidebar.image(Image.open("Images/Personal_Photo.jpg"), use_column_width = True)
        st.sidebar.markdown("""
        <center>
            <h1>Nathan Lawira</h1>
            <p>Senior Undergraduate Student in <b>Nanyang Technological University</b></p>
            <p>Pursuing a <b>Bachelor of Engineering in Chemical & Biomolecular Engineering</b> Specializing in Intellectual Property with a Minor in Modern Languages</p>
            <p>Expected to graduate in 2024</p>
        </center>
        """, unsafe_allow_html=True)

        # Social Media Links
        st.sidebar.markdown("""
        <div style="display: flex; justify-content: center;">
            <a href='mailto:nathanlawira@gmail.com'><img src='https://static.vecteezy.com/system/resources/previews/020/009/614/original/email-and-mail-icon-black-free-png.png' width='30' style='margin-right: 20px;'></a>
            <a href='https://www.linkedin.com/in/nathan-lawira/'><img src='https://img.icons8.com/color/48/000000/linkedin.png' width='30' style='margin-right: 20px;'></a>      
            <a href='https://www.instagram.com/nlawira/'><img src='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/600px-Instagram_icon.png' width='30'></a>
        </div>
        """, unsafe_allow_html=True)

    # Page Selection
    st.sidebar.write("---")
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