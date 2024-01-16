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
        st.markdown('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap">', unsafe_allow_html=True)
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
        # --- WORK EXPERIENCE ---
        st.write("---")
        st.subheader("Work Experience")

        # Data for Work Experience
        work_experience_data = {
            'Company': ['KMPG Services Pte. Ltd. (Singapore)', 'Pfizer Asia Pacific Pte. Ltd. (Singapore)'],
            'Start': ['2022-05', '2023-01'],
            'Finish': ['2022-07', '2023-07'],
            'Description': [
                'Interned as a **Management Intern** in the **R&D and Grants Consulting Team**',
                'Interned as a **Production Intern** in **Process Centric Team 1 (PCT1)**',
                ]
        }

        # Create a DataFrame
        df_work_experience = pd.DataFrame(work_experience_data)

        # Convert date columns to datetime
        df_work_experience['Start'] = pd.to_datetime(df_work_experience['Start'])
        df_work_experience['Finish'] = pd.to_datetime(df_work_experience['Finish'])

        # Create a Gantt chart using Plotly Express
        fig_work = px.timeline(df_work_experience, x_start='Start', x_end='Finish', y='Company',
                        color='Company', labels={'Company': 'Job Title'},
                        title='',
                        category_orders={'Company': list(df_work_experience['Company'])},
                        height=400,
                        )

        # Customize the layout of the chart
        fig_work.update_layout(
            xaxis=dict(title='Timeline', showgrid=True, gridcolor='lightgray', zeroline=False),
            yaxis=dict(title='', showgrid=True, gridcolor='lightgray', zeroline=False),
            showlegend=False,
            hovermode=False,
            margin=dict(t=5, l=0, r=0, b=5),
        )

        # Display the chart
        st.plotly_chart(fig_work,use_container_width=True)

        # Display additional details
        for index, row in df_work_experience.iterrows():
            start_month = row['Start'].strftime('%B')  # %B represents the full month name
            finish_month = row['Finish'].strftime('%B')  # %B represents the full month name
            st.write(f"**{row['Company']} ({start_month} {row['Start'].year} - {finish_month} {row['Finish'].year}):** {row['Description']}")
        st.write('Please navigate to the "Work" tab via the sidebar to find out more about my achievements!')

    with st.container():
        # --- SKILLS ---
        st.write("---")
        st.subheader("Skills")

    with st.container():
        # --- EDUCATION ---
        st.write("---")
        st.subheader("Education")
        # Sample data for education history
        education_data = {
            'School': ['Cahaya Bangsa Classical School (Indonesia)','Nanyang Technological University (Singapore)'],
            'Start': ['2016-08', '2020-08'],
            'Finish': ['2020-06', '2024-06'],
            'Description': [
                'Earned a **High School Degree**',
                'Earned **Bachelor\'s of Engineering in Chemical & Biomolecular Engineering** with \
                a **Specialization in Intellectual Property** and a **Minor in Modern Languages**'
            ]
        }

        # Create a DataFrame
        df_education = pd.DataFrame(education_data)

        # Convert date columns to datetime
        df_education['Start'] = pd.to_datetime(df_education['Start'])
        df_education['Finish'] = pd.to_datetime(df_education['Finish'])

        # Create a Gantt chart using Plotly Express
        fig_education = px.timeline(df_education, x_start='Start', x_end='Finish', y='School',
                                    color='School', labels={'School': 'Education Level'},
                                    title='',
                                    category_orders={'School': list(df_education['School'])},
                                    height=400)

        # Customize the layout of the chart
        fig_education.update_layout(
            xaxis=dict(title='Timeline', showgrid=True, gridcolor='lightgray', zeroline=False),
            yaxis=dict(title='', showgrid=True, gridcolor='lightgray', zeroline=False),
            showlegend=False,
            hovermode=False,
            margin=dict(t=5, l=0, r=0, b=5),
        )

        # Display the chart
        st.plotly_chart(fig_education, use_container_width = True)
 
        # Display additional details
        for index, row in df_education.iterrows():
            start_month = row['Start'].strftime('%B')  # %B represents the full month name
            finish_month = row['Finish'].strftime('%B')  # %B represents the full month name
            st.write(f"**{row['School']} ({start_month} {row['Start'].year} - {finish_month} {row['Finish'].year}):** {row['Description']}")
        st.write('Please navigate to the "Education" tab via the sidebar to find out more about my projects and co-curricular activities!')
    
    # --- PERSONALITY ---
    with st.container():
        st.write("---")
        st.subheader("Personality")
        with st.container():
            # MBTI Type and Description and Last Taken
            mbti_type = "Myers-Briggs Type Indicator (MBTI): Architect (INTJ-T)"
            mbti_description = "Architects are imaginative and strategic thinkers, with a plan for everything. \
                These thoughtful tacticians love perfecting the details of life, applying creativity and rationality. \
                They embrace rationality and impartiality, excelling in intellectual debates and scientific or technological fields. \
                They are fiercely independent, open-minded, and strong-willed."
            last_taken_mbti = "Test was taken on June 20, 2022 via 16personalities."
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
                'Extraverted': '#b2d7e3',
                'Introverted': '#4298b4',
                'Intuitive': '#e4ae3a',
                'Observant': '#f4dfb0',
                'Thinking': '#33a474',
                'Feeling': '#a5e3c9',
                'Judging': '#88619a',
                'Prospecting': '#d0bfd7',
                'Assertive': '#fabfc0',
                'Turbulent': '#f25e62',
            }

            # Creating the plotly bar graph
            fig_mbti = px.bar(
                df, 
                x="Values", 
                y="Category", 
                color="Subcategory", 
                orientation='h', 
                text='Text', 
                category_orders={"Category": category_order},
                color_discrete_map = color_map,
            )
            fig_mbti.update_traces(textfont=dict(size=15))
            fig_mbti.update_layout(
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
            st.plotly_chart(fig_mbti, use_container_width=True)
            st.write(last_taken_mbti)

        st.write("")
        st.write("")
        
        with st.container():
            # DISC Type and Description and Last Taken
            disc_type = "DISC Personality: Conscientiousness & Steadiness"
            last_taken_disc = "Test was taken on January 16, 2024 via Truity."

            # Replace the following with your actual DISC personality scores
            data = dict(
                trait=['Dominance', 'Influence', 'Steadiness', 'Conscientiousness'],
                score=[50, 32.1, 78.2, 100],
                description=[
                    'Takes charge to get things done. Makes decisions and takes action.',
                    'Engages others and shares enthusiasm. Inspires and persuades others.',
                    'Is helpful and shows care for others. Looks for ways to assist and serve.',
                    'Works steadily within systems. Focuses on order, accuracy and precision.']
                    )
            
            # Find the index of the trait with the highest score
            max_score_index = data['score'].index(max(data['score']))

            fig_disc = px.line_polar(data, r='score', theta='trait', line_close=True)

            fig_disc.update_layout(
                polar=dict(radialaxis=dict(visible=True)),
                showlegend=False, 
                hovermode=False
            )

            # Display everything
            st.subheader(disc_type)
            st.plotly_chart(fig_disc,use_container_width=True)
            for trait, desc in zip(data['trait'], data['description']):
                st.write(f"**{trait}:** {desc}")
            st.write(last_taken_disc)

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