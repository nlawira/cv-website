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

# Defining Functions
def work_experience():
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
        xaxis_title_font=dict(size=20),
    )

    # Display the chart
    st.plotly_chart(fig_work,use_container_width=True)

    # Display additional details
    for index, row in df_work_experience.iterrows():
        start_month = row['Start'].strftime('%B')  # %B represents the full month name
        finish_month = row['Finish'].strftime('%B')  # %B represents the full month name
        st.write(f"- **{row['Company']} ({start_month} {row['Start'].year} - {finish_month} {row['Finish'].year}):** {row['Description']}")

def education_history():
    # Data for education history
    education_data = {
        'School': ['Cahaya Bangsa Classical School (Indonesia)','Nanyang Technological University (Singapore)','National University of Singapore (Singapore)'],
        'Start': ['2016-08', '2020-08', '2022-01'],
        'Finish': ['2020-06', '2024-06', '2022-06'],
        'Description': [
            'Earned a **High School Degree**',
            'Earned **Bachelor\'s of Engineering in Chemical & Biomolecular Engineering** with \
            a **Specialization in Intellectual Property** and a **Minor in Modern Languages**',
            'Local student exchange under the **Singapore Universities Student Exchange Program (SUSEP)**'
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
        xaxis_title_font=dict(size=20),
    )

    # Display the chart
    st.plotly_chart(fig_education, use_container_width = True)

    # Display additional details
    for index, row in df_education.iterrows():
        start_month = row['Start'].strftime('%B')  # %B represents the full month name
        finish_month = row['Finish'].strftime('%B')  # %B represents the full month name
        st.write(f"- **{row['School']} ({start_month} {row['Start'].year} - {finish_month} {row['Finish'].year}):** {row['Description']}")
        
# Defining Pages
def home():
    with st.container():
        # --- TITLE & SUMMARY ---
        st.title("Hello, I am Nathan! :wave:")
        st.subheader("Summary")
        st.write("I am a Chemical & Biomolecular Engineering student at Nanyang Technological University and will graduate in May 2024. \
                My academic background equips me with strong analytical, problem-solving, and \
                critical thinking skills, while my enthusiasm and passion for data analytics, coding, and software development \
                reflects my keen interest in leveraging technologies to address and solve complex challenges!")
        st.write("Eager to apply my skills, I am actively seeking a full-time position in data analytics, coding, or software-related \
                fields where I can provide my expertise to create lasting contributions and continuously improve and grow professionally!")
   
    with st.container():
        # --- WORK EXPERIENCE ---
        st.write("---")
        st.subheader("Work Experience")
        work_experience()
        st.write('Please navigate to the "Work" tab via the sidebar to find out more about my achievements!')

    with st.container():
        # --- SKILLS ---
        st.write("---")
        st.subheader("Skills")
        
        with st.container():
            # Digital Skills Sections
            st.subheader("Computer/Digital Skills")
            # Skills Data
            data = {
                'Skill': ['Python', 'Data Visualization', 'Machine Learning', 'Web Development', 'Communication'],
                'Proficiency': [90, 80, 75, 70, 85],
                'Description': [
                    'Proficient in Python programming language.',
                    'Experience in creating informative and visually appealing visualizations.',
                    'Familiarity with machine learning algorithms and frameworks.',
                    'Skills in building web applications using various technologies.',
                    'Strong communication and collaboration skills.'
                ]
            }

            df = pd.DataFrame(data)

            # Create radar chart
            fig = go.Figure()

            fig.add_trace(go.Scatterpolar(
                r=df['Proficiency'],
                theta=df['Skill'],
                fill='toself',
                text=df['Proficiency'],
                hoverinfo='text+theta',
                line=dict(color='rgba(50, 171, 96, 1.0)'),
                marker=dict(color='rgba(50, 171, 96, 1.0)', size=8),
            ))

            # Set layout
            fig.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                showlegend=False,
            )

            # Display description below the chart
            st.plotly_chart(fig,use_container_width=True)
            st.write("### Skill Descriptions:")
            for skill, description in zip(df['Skill'], df['Description']):
                st.write(f"- **{skill}:** {description}")

        # Space Divider
        st.write("")
        st.write("")

        with st.container():
            # Language Proficiency Section
            st.subheader("Language Proficiency")

            # Languages Data
            languages = ['English', 'Bahasa Indonesia', 'Korean', 'Chinese', 'Japanese']
            proficiency_levels = [5, 5, 2, 1, 1]

            # Mapping for custom colors (replace with your preferred colors)
            color_mapping = {
                5: '#69B34C', #Native/Bilingual
                4: '#ACB334', #Full Professional
                3: '#FAB733', #Professional
                2: '#FF8E15', #Limited Working
                1: '#FF0D0D', # Elementary
            }

            # Mapping for custom text labels on x-axis
            proficiency_labels = {
                5: 'Native/Bilingual',
                4: 'Full Professional',
                3: 'Professional',
                2: 'Limited Working',
                1: 'Elementary',
                0: 'None'
            }


            # Create a horizontal bar chart
            fig = go.Figure(go.Bar(
                x=proficiency_levels[::-1],
                y=languages[::-1],
                orientation='h',
                marker_color=[color_mapping[level] for level in proficiency_levels[::-1]],  # Color mapping
            ))

            # Set layout
            fig.update_layout(
                xaxis=dict(
                    ticktext=[proficiency_labels[level] for level in [5,4,3,2,1,0]],  # Text labels
                    tickvals=[5,4,3,2,1,0],  # Corresponding values
                ),
                title_text='',
                xaxis_title='Proficiency Level',
                yaxis_title='Language',
                showlegend=False,
                modebar_remove=['lasso', 'select','toimage', 'pan'],
                margin=dict(t=5, b=5),
                yaxis_title_font=dict(size=20),
                xaxis_title_font=dict(size=20),
            )

            # Display the bar chart
            st.plotly_chart(fig, use_container_width=True)

    with st.container():
        # --- EDUCATION ---
        st.write("---")
        st.subheader("Education")
        education_history()
        st.write('Please navigate to the "Education" tab via the sidebar to find out more about my education history!')
    
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
                margin=dict(t=5, b=5))
            
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

            # DISC Personality Data
            data = dict(
                trait=['Dominance', 'Influence', 'Steadiness', 'Conscientiousness'],
                score=[50, 32.1, 78.2, 100],
                percentage=[19.2, 12.3, 30.1, 38.4],
                description=[
                    'Takes charge to get things done. Makes decisions and takes action.',
                    'Engages others and shares enthusiasm. Inspires and persuades others.',
                    'Is helpful and shows care for others. Looks for ways to assist and serve.',
                    'Works steadily within systems. Focuses on order, accuracy and precision.']
                    )

            # Creating Polar Chart
            fig_disc1 = px.line_polar(data, r='score', theta='trait', line_close=True)
            fig_disc1.update_layout(
                polar=dict(radialaxis=dict(visible=True)),
                showlegend=False, 
                hovermode=False
            )

            # Creating Pie Chart
            colors = ['#D62728','#FFBF00', '#2CA02C',  '#1F77B4']
            fig_disc2 = go.Figure(data=[go.Pie(labels=data['trait'], values=data['percentage'], marker=dict(colors=colors))])
            fig_disc2.update_layout(
                title_text="",
                showlegend=False,
            )

            # Display everything
            st.subheader(disc_type)
            left, right = st.columns(2)
            with left:
                st.plotly_chart(fig_disc1)
            with right:
                st.plotly_chart(fig_disc2)
            for trait, desc in zip(data['trait'], data['description']):
                st.write(f"- **{trait}:** {desc}")
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
    st.title("Work Experience")
    with st.container():
        st.subheader("Summary")
        work_experience()
    st.write("- - -")
    # Pfizer Internship
    with st.container():
        st.subheader("Production, PCT1 - Intern at Pfizer Asia Pacific Pte. Ltd.")
        left,right = st.columns([2,1])
        with left:
            st.write("Some description here")
        with right:
            st.write("Some pictures here")
    # KPMG Internship
    with st.container():
        st.subheader("R&D and Grants Consulting - Management Intern at KPMG Services Pte. Ltd.")
        left,right = st.columns([1,2])
        with left:
            st.write("Some pictures here")
        with right:
            st.write("Some description here")
    return

def education():
    st.title("Education History")
    with st.container():
        st.subheader("Summary")
        education_history()
    st.write("- - -")
    # Academic Projects
    with st.container():
        st.subheader("Academic Projects")
        st.write("Some description here")
    st.write("- - -")
    # Relevant Classes/Modules
    with st.container():
        st.subheader("Relevant Classes/Modules")
        st.write("Some description here")
    # Online Courses
    with st.container():
        st.subheader("Online Courses")
        st.write("Some description here")
    return

def cca():
    st.title("Co-Curricular, Leadership, and Voluntary Activities")
    # NTU Piano Ensemble
    with st.container():
        st.subheader("NTU Piano Ensemble")
        st.caption("Logistics Director")
        st.caption("**Time Stamp Here**")
        st.caption("Associated with **Nanyang Technological University**")
        left,right=st.columns([2,1])
        with left:
            st.write("Some description here")
        with right:
            st.write("Some picture here")
    # ICN
    with st.container():
        st.subheader("Indonesian Cultural Night")
        st.caption("Corporate Liaison Officer")
        st.caption("**Time Stamp Here**")
        st.caption("Associated with **Nanyang Technological University**")
        left,right=st.columns([1,2])
        with left:
            st.write("Some picture here")
        with right:
            st.write("Some description here")
    # TMC Serikat
    with st.container():
        st.subheader("Toastmasters Club Serikat")
        st.caption("Vice President of Membership")
        st.caption("**Time Stamp Here**")
        st.caption("Associated with **Nanyang Technological University**")
        left,right=st.columns([2,1])
        with left:
            st.write("Some description here")
        with right:
            st.write("Some picture here")
    # NTU Earthlink
    with st.container():
        st.subheader("NTU Earthlink — Eco-Campus Portfolio")
        st.caption("Campaign Executive")
        st.caption("**Time Stamp Here**")
        st.caption("Associated with **Nanyang Technological University**")
        left,right=st.columns([1,2])
        with left:
            st.write("Some picture here")
        with right:
            st.write("Some description here")
    # NTUSU WIC
    with st.container():
        st.subheader("NTU Student Union — Welfare Initiatives Committee")
        st.caption("Logistics Officer")
        st.caption("**Time Stamp Here**")
        st.caption("Associated with **Nanyang Technological University**")
        left,right=st.columns([2,1])
        with left:
            st.write("Some description here")
        with right:
            st.write("Some picture here")
    # MUN Club
    with st.container():
        st.subheader("CBCS Model United Nations Club")
        st.caption("Board of Executive, President")
        st.caption("**Time Stamp Here**")
        st.caption("Associated with **Cahaya Bangsa Classical School**")
        left,right=st.columns([1,2])
        with left:
                st.write("Some picture here")
        with right:
                st.write("Some description here")
    # Yearbook Team
    with st.container():
        st.subheader("CBCS Yearbook Team")
        st.caption("Journalist")
        st.caption("**Time Stamp Here**")
        st.caption("Associated with **Cahaya Bangsa Classical School**")
        left,right=st.columns([2,1])
        with left:
                st.write("Some description here")
        with right:
                st.write("Some picture here")
    # Debate
    with st.container():
        st.subheader("CBCS Debate Club")
        st.caption("Member")
        st.caption("**Time Stamp Here**")
        st.caption("Associated with **Cahaya Bangsa Classical School**")
        left,right=st.columns([1,2])
        with left:
                st.write("Some picture here")
        with right:
                st.write("Some description here")
    return

def hobbies():
    st.title("Hobbies & Personal Life")
    # Learning New Languages
    with st.container():
        st.subheader("Learning New Languages")
        left,right=st.columns([2,1])
        with left:
            st.write("Some description here")
        with right:
            st.write("Some picture here")
    # Photography
    with st.container():
        st.subheader("Photography")
        left,right=st.columns([1,2])
        with left:
            st.write("Some picture here")
        with right:
             st.write("Some description here")
    # Music
    with st.container():
        st.subheader("Listening & Playing Music")
        left,right=st.columns([2,1])
        with left:
            st.write("Some description here")
        with right:
            st.write("Some picture here")
    # Reading
    with st.container():
        st.subheader("Reading")
        left,right=st.columns([1,2])
        with left:
            st.write("Some picture here")
        with right:
             st.write("Some description here")
    # Exercising
    with st.container():
        st.subheader("Exercising")
        left,right=st.columns([2,1])
        with left:
            st.write("Some description here")
        with right:
            st.write("Some picture here")
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
            <p>Expected to graduate in <b>May 2024</b></p>
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