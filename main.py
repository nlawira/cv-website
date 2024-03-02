# Importing necessary libraries
import streamlit as st
from streamlit_lottie import st_lottie
import requests
import plotly.graph_objs as go
from PIL import Image
import plotly.express as px
import pandas as pd
from pdf2image import convert_from_path

# Initial Settings
st.set_page_config(page_title="My Webpage", layout="wide")

# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap">', unsafe_allow_html=True)
        st.markdown(f"<style>{f.read()}</style/", unsafe_allow_html=True)
local_css("Style/style.css")

# Defining Experience/History
def work_experience():
    # Data for Work Experience
    work_experience_data = {
        'Company': ['Pfizer Asia Pacific Pte. Ltd., Singapore', 'KMPG Services Pte. Ltd., Singapore'],
        'Start': ['2023-01', '2022-05'],
        'Finish': [ '2023-07', '2022-07'],
        'Description': [
            'Interned as a **Production Intern** in **Process Centric Team 1 (PCT1)**',
            'Interned as a **Management Intern** in the **R&D and Grants Consulting Team**',
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
        'School': ['Nanyang Technological University, Singapore','National University of Singapore, Singapore','Cahaya Bangsa Classical School, Indonesia'],
        'Start': ['2020-08', '2022-01', '2016-08'],
        'Finish': ['2024-06', '2022-06', '2020-06'],
        'Description': [
            'To earn **Bachelor\'s of Engineering (Honours) in Chemical & Biomolecular Engineering** with \
            a **Specialization in Intellectual Property** and a **Minor in Modern Languages**',
            'Local student exchange under the **Singapore Universities Student Exchange Program (SUSEP)**',
            'Earned a **High School Degree**',
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

# Function to change the image index
def change_image_1(delta, images):
    st.session_state.index_1 = (st.session_state.index_1 + delta) % len(images)
def change_image_2(delta, images):
    st.session_state.index_2 = (st.session_state.index_2 + delta) % len(images)
def change_image_3(delta, images):
    st.session_state.index_3 = (st.session_state.index_3 + delta) % len(images)
def change_image_4(delta, images):
    st.session_state.index_4 = (st.session_state.index_4 + delta) % len(images)
def change_image_5(delta, images):
    st.session_state.index_5 = (st.session_state.index_5 + delta) % len(images)
def change_image_6(delta, images):
    st.session_state.index_6 = (st.session_state.index_6 + delta) % len(images)
def change_image_7(delta, images):
    st.session_state.index_7 = (st.session_state.index_7 + delta) % len(images)
def change_image_8(delta, images):
    st.session_state.index_8 = (st.session_state.index_8 + delta) % len(images)

# Converting PDF to Images
def convert_pdf_to_images(pdf_path):
    # Convert PDF to a list of images
    images = convert_from_path(pdf_path)
    return images

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
        st.write("Eager to apply my skills, I am actively seeking a full-time position in analyst, data science, and any-related roles where \
                 I can provide my skills and expertise in coding and data analysis to create lasting contributions and continuously improve and grow professionally!")
   
    with st.container():
        # --- WORK EXPERIENCE ---
        st.write("---")
        st.subheader("Work Experience")
        work_experience()
        st.write('Please navigate to the **Work** tab via the sidebar to find out more about my achievements!')

    with st.container():
        # --- SKILLS ---
        st.write("---")
        st.subheader("Skills")
        
        with st.container():
            # Digital Skills Sections
            st.subheader("Computer/Digital Skills")
            
            st.write("This section is still a work-in-progress. Sorry!")

        #     # Skills Data
        #     data = {
        #         'Skill': ['Python', 'Data Visualization', 'Machine Learning', 'Web Development', 'Communication'],
        #         'Proficiency': [90, 80, 75, 70, 85],
        #         'Description': [
        #             'Proficient in Python programming language.',
        #             'Experience in creating informative and visually appealing visualizations.',
        #             'Familiarity with machine learning algorithms and frameworks.',
        #             'Skills in building web applications using various technologies.',
        #             'Strong communication and collaboration skills.'
        #         ]
        #     }

        #     df = pd.DataFrame(data)

        #     # Create radar chart
        #     fig = go.Figure()

        #     fig.add_trace(go.Scatterpolar(
        #         r=df['Proficiency'],
        #         theta=df['Skill'],
        #         fill='toself',
        #         text=df['Proficiency'],
        #         hoverinfo='text+theta',
        #         line=dict(color='rgba(50, 171, 96, 1.0)'),
        #         marker=dict(color='rgba(50, 171, 96, 1.0)', size=8),
        #     ))

        #     # Set layout
        #     fig.update_layout(
        #         polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        #         showlegend=False,
        #     )

        #     # Display description below the chart
        #     st.plotly_chart(fig,use_container_width=True)
        #     st.write("### Skill Descriptions:")
        #     for skill, description in zip(df['Skill'], df['Description']):
        #         st.write(f"- **{skill}:** {description}")

        # Space Divider
        st.write("")
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
        st.write('Please navigate to the **Education** tab via the sidebar to find out more about my education history!')
    
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

        # Space Divider
        st.write("")
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
            left, right = st.columns([1.25,1])
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
        st.subheader("Pfizer Asia Pacific Pte. Ltd.")
        left,right = st.columns([1.5,1])
        with left:
            st.write("**Production, PCT1 - Intern**")
            st.caption("**Jan 2023 - Jul 2023**")
            st.write("- Resolved a product's out-of-specification (OOS) deviation by data mining and analysis, \
                     **leading to the implementation of corrective and preventive actions**\n",
                     "- Developed a Python code to automate the reporting daily alarms in \
                        Pfizer Tuas API & Solvent Recovery Plant, **reducing reporting time by approximately 90%**\n",
                     "- Designed a matrix for equipment and process lines to prevent clashes and support more efficienct \
                        and precise planning in production and changeover, **improving planning efficiency by 500%**\n",
                     "- Collaborated with alarm management and continuous improvement teams for \
                        alarm reporting and reduction initiatives, **eliciting reclassification and reduction of over 50 alarms** \
                        to reduce alarm fatigue experienced by technicians\n",
                     "- Supported the process engineers in day-to-day activities, including **over 15 batch books \
                        review**, **over 20 batch data documentations**, and process issues troubleshooting")
        with right:
            st.image(Image.open("Images/Pfizer_1.png"), use_column_width = True)
    
    # Space Divider
    st.write("")
    st.write("")
    
    # KPMG Internship
    with st.container():
        st.subheader("KPMG Services Pte. Ltd.")
        left,right = st.columns([1,1.5])
        with left:
            st.image(Image.open("Images/KPMG_1.png"), use_column_width = True)
        with right:
            st.write("**R&D and Grants Consulting - Management Intern**")
            st.caption("**May 2022 - Jul 2022**")
            st.write("- Updated **8 letter templates and claims forms** used in engagements and recordkeeping\n",
                     "- Researched and collated information about clients’ R&D projects, grants & incentives, \
                        and potential competitors for **7 engagements**\n",
                     "- Facilitated the creation of slide decks used in **5 engagements** to formulate an R&D storyline to fulfill tax incentives requirements\n",
                     "- Conducted risk assessments for **5 engagements** to completion")
    return

def education():
    st.title("Education History")
    with st.container():
        st.subheader("Summary")
        education_history()
    st.write("- - -")
    
    # NTU
    with st.container():
        st.subheader("Nanyang Technological University, Singapore (NTU)")
        left,right = st.columns([1.5,1])
        with left:
            st.write("**Bachelor's of Engineering (Honours)**")
            st.caption("**Aug 2020 - Jun 2024 (Expected)**")
            st.write("- Major: **Chemical & Biomolecular Engineering**\n",
                     "- CGPA: **4.47/5.00** (As of end of 2023)\n",
                     "- Currently pursuing a **Specialization in Intellectual Property** and a **Minor in Modern Languages**\n",
                     "- **Actively involved in leadership positions** across various CCAs and clubs")
        with right:
            # Defining image paths and loading them
            image_paths = ["Images/NTU_1.png", "Images/NTU_2.jpg", "Images/NTU_3.jpg", "Images/NTU_4.jpg"]
            images = [Image.open(image_path) for image_path in image_paths]

            # Session state to store the current image index
            if 'index_1' not in st.session_state:
                st.session_state.index_1 = 0

            # Display the current image
            st.image(images[st.session_state.index_1], width=350)

            # Create two columns for the arrows
            prev, _, next = st.columns([1, 1, 1])

            with prev:
                # Left arrow button
                st.button('Prev', key='prev_1', on_click=change_image_1, args=(-1, images))

            with next:
                # Right arrow button
                st.button('Next', key='next_1', on_click=change_image_1, args=(1, images))

    
    # Space Divider
    st.write("")
    st.write("")
    st.write("")
    
    # NUS
    with st.container():
        st.subheader("National University of Singapore, Singapore (NUS)")
        left,right = st.columns([1,1.5])
        with left:
            # Defining image paths and loading them
            image_paths = ["Images/NUS_1.png", "Images/NUS_2.jpg"]
            images = [Image.open(image_path) for image_path in image_paths]

            # Session state to store the current image index
            if 'index_2' not in st.session_state:
                st.session_state.index_2 = 0

            # Display the current image
            st.image(images[st.session_state.index_2], width=350)

            # Create two columns for the arrows
            prev, _, next = st.columns([1, 1, 1])

            with prev:
                # Left arrow button
                st.button('Prev', key='prev_2', on_click=change_image_2, args=(-1, images))

            with next:
                # Right arrow button
                st.button('Next', key='next_2', on_click=change_image_2, args=(1, images))
        with right:
            st.write("**Exchange Program**")
            st.caption("**Jan 2022 - Jun 2022**")
            st.write("- Exchanged under the **Singaporean Universities Student Exchange Program (SUSEP)**\n",
                     "- Exposed to a new educational environment and student community\n",
                     "- Expanded network and made new connections with NUS students")

        
    # Space Divider
    st.write("")
    st.write("")
    st.write("")

    # CBCS        
    with st.container():
        st.subheader("Cahaya Bangsa Classical School, Indonesia (CBCS)")
        left,right = st.columns([1.5,1])
        with left:
            st.write("**Indonesian High School Degree**")
            st.caption("**Aug 2016 - Jun 2020**")
            st.write("- Final CGPA: **3.782/4.000**\n",
                     "- Proved academic excellence and achieved **Valedictorian** award for Class of 2020 Natural Science track\n",
                     "- **Actively involved** in various student clubs and activities")
        with right:
            # Defining image paths and loading them
            image_paths = ["Images/CBCS_1.png", "Images/CBCS_2.jpg", "Images/CBCS_3.jpg", "Images/CBCS_4.jpg"]
            images = [Image.open(image_path) for image_path in image_paths]

            # Session state to store the current image index
            if 'index_3' not in st.session_state:
                st.session_state.index_3 = 0

            # Display the current image
            st.image(images[st.session_state.index_3], width=350)

            # Create two columns for the arrows
            prev, _, next = st.columns([1, 1, 1])

            with prev:
                # Left arrow button
                st.button('Prev', key='prev_3', on_click=change_image_3, args=(-1, images))

            with next:
                # Right arrow button
                st.button('Next', key='next_3', on_click=change_image_3, args=(1, images))
    st.write("- - -")

    # Academic Projects
    st.subheader("Academic Projects")
    with st.container():
        st.subheader("Final Year Design Project (FYDP)")
        st.write("On the topic of **Biomass Wastes Valorization to Platform Chemicals**")
        st.caption("**Jan 2024 -  May 2024 (Expected)**")
        st.caption("Associated with **Nanyang Technological University**")
        st.write("-	Developing a **sustainable production line processing biomass wastes into furfural and acids** via Aspen Plus and HYSYS\n",
                 "- **Collaborating with a group of 6 people** in designing the simulation, reviewing literature, and conducting cost and market analysis")
    with st.container():
        st.subheader("Senior Thesis Defence")
        st.write("On the topic of **Diving Deeper into Indonesia's Voting Age and Being Politically Informed**")
        st.caption("**Aug 2019 -  May 2020**")
        st.caption("Associated with **Cahaya Bangsa Classical School**")
        st.write("This part is still a work-in-progress. Sorry!")
    with st.container():
        st.subheader("Karya Ilmiah (Indonesian Thesis Defence)")
        st.write("On the topic of **Article 222 Law No. 7 of 2017 Governing Elections (Presidential Threshold)**")
        st.caption("**Aug 2018 -  May 2019**")
        st.caption("Associated with **Cahaya Bangsa Classical School**")
        st.caption("Delivered in **Bahasa Indonesia**")
        st.write("This part is still a work-in-progress. Sorry!")
    st.write("- - -")
    
    # Relevant Classes/Modules
    st.subheader("Relevant Classes/Modules")
    st.write("")

    #CB4247
    with st.container():
        st.subheader("CB4247 Statistics & Computational Inference to Big Data")
        left,right=st.columns([1.5,1])
        with left:
            st.caption("**2023-2024 Semester 2**")
            st.caption("Associated with **Nanyang Technological University**")
            st.write("This part is still a work-in-progress. Sorry!")
        with right:
            st.write("")
    
    # Space Divider
    st.write("")
    st.write("")
    st.write("")

    #CB0494
    with st.container():
        st.subheader("CB0494 Introduction to Data Science and Artificial Intelligence")
        left,right=st.columns([1,1.5])
        with left:
            st.write("")
        with right:
            st.caption("**2021-2022 Semester 2**")
            st.caption("Associated with **Nanyang Technological University**")
            st.write("This part is still a work-in-progress. Sorry!")

    #CH2010
    with st.container():
        st.subheader("CH2010 Engineering Statistics")
        left,right=st.columns([1.5,1])
        with left:
            st.caption("**2021-2022 Semester 1**")
            st.caption("Associated with **Nanyang Technological University**")
            st.write("This part is still a work-in-progress. Sorry!")
        with right:
            st.write("")

    st.write("- - -")
    
    # Online Courses
    with st.container():
        st.subheader("Online Courses")
        st.write("This part is still a work-in-progress. Sorry!")
        left, right = st.columns(2)
        with left:
            # Path to PDF File
            pdf_path = "Images/Advanced_Python.pdf"
            image = convert_pdf_to_images(pdf_path)
            st.image(image, use_column_width=True)
        with right:
            pdf_path = "Images/Applied Social Network Analysis in Python.pdf"
            image = convert_pdf_to_images(pdf_path)
            st.image(image, use_column_width=True)
    return

def cca():
    st.title("Co-Curricular and Leadership Activities")
    # NTU Piano Ensemble
    with st.container():
        st.subheader("NTU Piano Ensemble")
        left,right=st.columns([1.5,1])
        with left:
            st.write("**Logistics Director**")
            st.caption("**Aug 2021 - Jul 2023**")
            st.caption("Associated with **Nanyang Technological University**")
            st.write("- Directed the logistics, including transportation of instruments, stage planning, \
                     and equipment tracking, for **8 concerts**\n",
                     "- Processed **over 30 bookings** for the music room weekly\n",
                     "- Supervised providing logistical support for NTU Symphony Orchestra, NTU Chinese Orchestra, and NTU \
                        Symphonic Band in **NTUPE's first inter-CCA concert**\n",
                     "- Organized and manned the physical and virtual booths for NTUSU and CAC Welcome Week, achieving \
                        **over 100 new members per year**\n",
                     "- **Resolved an issue** regarding members' access to NTUPE facilities by partnering \
                        with Nanyang House administrators and NTU Student Affairs Office\n",
                     "- Managed NTUPE inventory and equipment lending to other CCAs")
        with right:
            # Defining image paths and loading them
            image_paths = ["Images/NTUPE_1.png", "Images/NTUPE_2.PNG"]
            images = [Image.open(image_path) for image_path in image_paths]

            # Session state to store the current image index
            if 'index_1' not in st.session_state:
                st.session_state.index_1 = 0

            # Display the current image
            st.image(images[st.session_state.index_1], width=350)

            # Create two columns for the arrows
            prev, _, next = st.columns([1, 1, 1])

            with prev:
                # Left arrow button
                st.button('Prev', key='prev_1', on_click=change_image_1, args=(-1, images))

            with next:
                # Right arrow button
                st.button('Next', key='next_1', on_click=change_image_1, args=(1, images))
    
    # Space Divider
    st.write("")
    st.write("")
    st.write("")
    
    # ICN
    with st.container():
        st.subheader("Indonesian Cultural Night")
        left,right=st.columns([1,1.5])
        with left:
            # Defining image paths and loading them
            image_paths = ["Images/ICN_1.png", "Images/ICN_2.jpg", "Images/ICN_3.jpg"]
            images = [Image.open(image_path) for image_path in image_paths]

            # Session state to store the current image index
            if 'index_2' not in st.session_state:
                st.session_state.index_2 = 0

            # Display the current image
            st.image(images[st.session_state.index_2], width=350)

            # Create two columns for the arrows
            prev, _, next = st.columns([1, 1, 1])

            with prev:
                # Left arrow button
                st.button('Prev', key='prev_2', on_click=change_image_2, args=(-1, images))

            with next:
                # Right arrow button
                st.button('Next', key='next_2', on_click=change_image_2, args=(1, images))
        with right:
            st.write("**Corporate Liaison Officer**")
            st.caption("**Aug 2022 -  Jun 2023**")
            st.caption("Associated with **Nanyang Technological University**")
            st.write("- Created and distributed **21 sponsorship proposals** to various companies\n",
                     "- **Led a team of 14 people** working in NUS Run Big 2022 as paid volunteers \
                     to raise funds for the final show\n",
                     "- **Led a team of 22 people** working in Standard Chartered Singapore Marathon 2022 \
                     as paid volunteers to raise funds for the final show\n",
                     "- Managed the flower sales booth during the day of the final show")
    
    # Space Divider
    st.write("")
    st.write("")
    st.write("")    
    
    # TMC Serikat
    with st.container():
        st.subheader("Toastmasters Club Serikat")
        left,right=st.columns([1.5,1])
        with left:
            st.write("**Vice President of Membership**")
            st.caption("**Jan 2022 - Dec 2022**")
            st.caption("Associated with **Nanyang Technological University**")
            st.write("- Earned an **additional 13 members**, on top of **7 executive committee members**, by advertising \
                     through Indonesian students’ channels throughout Singapore, thereby chartering the club\n",
                     "- Obtained a vouch **through collaboration with PPI Singapura**\n",
                     "- Hosted every Zoom chapter meeting and handled logistics including creating polls, \
                        spotlighting speakers, and accommodating speakers and guests\n",
                     "- Spearhead publicizing of chapter meetings, **obtaining an average of 3 guests** for each meeting\n",
                     "- Managed Telegram group of over **40 members and guests**")
        with right:
            # Defining image paths and loading them
            image_paths = ["Images/TMC_Serikat_1.png", "Images/TMC_Serikat_2.jpg", "Images/TMC_Serikat_3.jpg", "Images/TMC_Serikat_4.jpg"]
            images = [Image.open(image_path) for image_path in image_paths]

            # Session state to store the current image index
            if 'index_3' not in st.session_state:
                st.session_state.index_3 = 0

            # Display the current image
            st.image(images[st.session_state.index_3], width=350)

            # Create two columns for the arrows
            prev, _, next = st.columns([1, 1, 1])

            with prev:
                # Left arrow button
                st.button('Prev', key='prev_3', on_click=change_image_3, args=(-1, images))

            with next:
                # Right arrow button
                st.button('Next', key='next_3', on_click=change_image_3, args=(1, images))
    
    # Space Divider
    st.write("")
    st.write("")
    st.write("")

    # NTU Earthlink
    with st.container():
        st.subheader("NTU Earthlink — Eco-Campus Portfolio")
        left,right=st.columns([1,1.5])
        with left:
            st.image(Image.open("Images/Earthlink_1.jpg"), width = 350)
        with right:
            st.write("**Campaign Executive**")
            st.caption("**Aug 2021 - Jun 2022**")
            st.caption("Associated with **Nanyang Technological University**")
            st.write("- Cooperated with a team to **improve 4 existing campaigns**, promoting eco-friendly campus living\n",
                     "- Brainstormed and conducted the written content creation for **4 campaigns**\n",
                     "- Directed \"See It Yourself\" campaign's video content to raise awareness amongst NTU \
                        population about correct recycling practices and collaboration with susGain")
    
    # Space Divider
    st.write("")
    st.write("")
    st.write("")

    # NTUSU WIC
    with st.container():
        st.subheader("NTU Student Union — Welfare Initiatives Committee")
        left,right=st.columns([1.5,1])
        with left:
            st.write("**Logistics Officer**")
            st.caption("**Aug 2021 -  Jun 2022**")
            st.caption("Associated with **Nanyang Technological University**")
            st.write("- Collaborated in a **team of 5-8 members** to plan welfare events for NTU students\n",
                     "- Implemented ideas for engagement activities and welfare items for **4 university-wide welfare events**\n",
                     "- Supervised the logistics and transport of equipment for **4 university-wide welfare events**")
        with right:
            # Defining image paths and loading them
            image_paths = ["Images/WIC_1.png", "Images/WIC_2.jpg"]
            images = [Image.open(image_path) for image_path in image_paths]

            # Session state to store the current image index
            if 'index_4' not in st.session_state:
                st.session_state.index_4 = 0

            # Display the current image
            st.image(images[st.session_state.index_4], width=350)

            # Create two columns for the arrows
            prev, _, next = st.columns([1, 1, 1])

            with prev:
                # Left arrow button
                st.button('Prev', key='prev_4', on_click=change_image_4, args=(-1, images))

            with next:
                # Right arrow button
                st.button('Next', key='next_4', on_click=change_image_4, args=(1, images))
    
    # Space Divider
    st.write("")
    st.write("")
    st.write("")  
    
    # MUN Club
    with st.container():
        st.subheader("Model United Nations (MUN) Club")
        left,right=st.columns([1,1.5])
        with left:
            # Defining image paths and loading them
            image_paths = ["Images/CBCS_1.png", "Images/MUN_1.jpg", "Images/MUN_2.jpg", "Images/MUN_3.jpg", "Images/MUN_4.jpeg"]
            images = [Image.open(image_path) for image_path in image_paths]

            # Session state to store the current image index
            if 'index_5' not in st.session_state:
                st.session_state.index_5 = 0

            # Display the current image
            st.image(images[st.session_state.index_5], width=350)

            # Create two columns for the arrows
            prev, _, next = st.columns([1, 1, 1])

            with prev:
                # Left arrow button
                st.button('Prev', key='prev_5', on_click=change_image_5, args=(-1, images))

            with next:
                # Right arrow button
                st.button('Next', key='next_5', on_click=change_image_5, args=(1, images))
        with right:
            st.write("**Board of Executive, President**")
            st.caption("**Aug 2019 - Jun 2020**")
            st.caption("Associated with **Cahaya Bangsa Classical School**")
            st.write("- Marketed the club throughout school, **obtaining 15+ new members**\n",
                     "- **Mentored 15+ members** on MUN protocols and procedures, drafting position papers, and \
                        effective speech delivery\n",
                     "- **Conducted \"Conference Zero\" prior to every competition** to train and prepare participants")
    
    # Space Divider
    st.write("")
    st.write("")
    st.write("")   
    
    # Yearbook Team
    with st.container():
        st.subheader("Yearbook Team")
        left,right=st.columns([1.5,1])
        with left:
            st.write("**Journalist**")
            st.caption("**Aug 2019 - Jun 2020**")
            st.caption("Associated with **Cahaya Bangsa Classical School**")
            st.write("- Coordinated interviews with teachers and students for yearbook content\n",
                     "- Compiled teachers' testimonies of their teaching experience and students' school life\n",
                     "- Proofread yearbook for grammar and spelling mistakes before release")
        with right:
            st.image(Image.open("Images/CBCS_1.png"), width = 350)
    
    # Space Divider
    st.write("")
    st.write("")
    st.write("")   
    
    # Debate
    with st.container():
        st.subheader("CBCS Debate Club")
        left,right=st.columns([1,1.5])
        with left:
            # Defining image paths and loading them
            image_paths = ["Images/CBCS_1.png", "Images/Debate_1.jpg", "Images/Debate_1.jpg"]
            images = [Image.open(image_path) for image_path in image_paths]

            # Session state to store the current image index
            if 'index_6' not in st.session_state:
                st.session_state.index_6 = 0

            # Display the current image
            st.image(images[st.session_state.index_6], width=350)

            # Create two columns for the arrows
            prev, _, next = st.columns([1, 1, 1])

            with prev:
                # Left arrow button
                st.button('Prev', key='prev_6', on_click=change_image_6, args=(-1, images))

            with next:
                # Right arrow button
                st.button('Next', key='next_6', on_click=change_image_6, args=(1, images))
        with right:
            st.write("**Founding Member**")
            st.caption("**Aug 2017 - Jun 2019**")
            st.caption("Associated with **Cahaya Bangsa Classical School**")
            st.write("- Participated in numerous Asian Parliamentary debate competitions as the team's first speaker\n",
                     "- **Achieved quarterfinalists awards** in Phyxius English Debating Competition 2017 and 2018\n",
                     "- Analyzed past debate performances to identify strengths and weaknesses, formulating strategies for future competitions")
    st.write("- - -")
    
    # Voluntary Activities
    st.title("Voluntary Activities")

    # New Life 
    with st.container():
        st.subheader("New Life Community Services")
        left,right=st.columns([1.5,1])
        with left:
            st.write("**English Teacher**")
            st.caption("**Feb 2023 - May 2023, Sep 2023 - Dec 2023**")
            st.write("- Designed teaching program, learning materials, and syllabus to teach **12-15 Indonesian \
                     migrant workers** in Singapore aged 20 to 40 years old, successly advancing English speaking proficiency\n",
                     "- Worked together with a **team of 4-5 members** to deliver teaching content biweekly\n"
                     "- Planned overall timeline and monthly meetings")
        with right:
            # Defining image paths and loading them
            image_paths = ["Images/English_Teaching_1.png", "Images/English_Teaching_2.jpg", "Images/English_Teaching_3.jpg"]
            images = [Image.open(image_path) for image_path in image_paths]

            # Session state to store the current image index
            if 'index_7' not in st.session_state:
                st.session_state.index_7 = 0

            # Display the current image
            st.image(images[st.session_state.index_7], width=350)

            # Create two columns for the arrows
            prev, _, next = st.columns([1, 1, 1])

            with prev:
                # Left arrow button
                st.button('Prev', key='prev_7', on_click=change_image_7, args=(-1, images))

            with next:
                # Right arrow button
                st.button('Next', key='next_7', on_click=change_image_7, args=(1, images))

    # NTU CCEB OCEP
    with st.container():
        st.subheader("NTU CCEB's Overseas Community Engagement Project")
        left,right=st.columns([1,1.5])
        with left:
            st.image(Image.open("Images/CCEB_1.png"), width = 350)
        with right:
            st.write("**Student Volunteer in Project T. A. B.**")
            st.caption("**Aug 2021 - Dec 2021**")
            st.caption("Associated with **Nanyang Technological University**")
            st.write("- **Headed a team of 4 people** to create educational content for Spright Academy students on mental health\n",
                     "- **Delegated specific tasks to group members**, ensuring contributions were met for collaborative review\n",
                     "- **Organized regular online meetings** to discuss and refine content, aiming for seamless integration and flow")
    
    # Kalimantan
    with st.container():
        st.subheader("Living Waters Village (Kalimantan)")
        left,right=st.columns([1.5,1])
        with left:
            st.write("**Student Volunteer**")
            st.caption("**Apr 2019 - May 2019**")
            st.caption("Associated with **Cahaya Bangsa Classical School**")
            st.write("- **Engaged in a 10-day volunteer program** serving and teaching the children of the Dayak tribe\n",
                     "- Assisting the adults with day-to-day labor activities, such as construction, farming, and cooking")
        with right:
            # Defining image paths and loading them
            image_paths = ["Images/LWV_1.jpg", "Images/LWV_2.JPG", "Images/LWV_3.JPG"]
            images = [Image.open(image_path) for image_path in image_paths]

            # Session state to store the current image index
            if 'index_8' not in st.session_state:
                st.session_state.index_8 = 0

            # Display the current image
            st.image(images[st.session_state.index_8], width=350)

            # Create two columns for the arrows
            prev, _, next = st.columns([1, 1, 1])

            with prev:
                # Left arrow button
                st.button('Prev', key='prev_8', on_click=change_image_8, args=(-1, images))

            with next:
                # Right arrow button
                st.button('Next', key='next_8', on_click=change_image_8, args=(1, images))

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

    # Space Divider
    st.write("")
    st.write("")
    st.write("")

    # Photography
    with st.container():
        st.subheader("Photography")
        left,right=st.columns([1,2])
        with left:
            st.write("Some picture here")
        with right:
             st.write("Some description here")
    
    # Space Divider
    st.write("")
    st.write("")
    st.write("")    
    
    # Music
    with st.container():
        st.subheader("Listening & Playing Music")
        left,right=st.columns([2,1])
        with left:
            st.write("Some description here")
        with right:
            st.write("Some picture here")
    
    # Space Divider
    st.write("")
    st.write("")
    st.write("")
    
    # Reading
    with st.container():
        st.subheader("Reading")
        left,right=st.columns([1,2])
        with left:
            st.write("Some picture here")
        with right:
             st.write("Some description here")
    
    # Space Divider
    st.write("")
    st.write("")
    st.write("")    
    
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
        st.sidebar.image(Image.open("Images/Personal_Photo.JPG"), use_column_width = True)
        st.sidebar.markdown("""
        <center>
            <h1>Nathan Lawira</h1>
            <p>Senior Undergraduate Student in <b>Nanyang Technological University</b></p>
            <p>Pursuing a <b>Bachelor of Engineering in Chemical & Biomolecular Engineering</b> Specializing in Intellectual Property with a Minor in Modern Languages</p>
            <p>Expected to graduate in <b>June 2024</b></p>
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
    page = st.sidebar.selectbox('Select Page', 
                                ["Home",
                                 "Work",
                                 "Education",
                                 "Co-Curricular, Leadership & Voluntary Activies",
                                 ],
                                 index=0)
    if page == "Home":
        home()
    if page == "Work":
        work()
    if page == "Education":
        education()
    if page == "Co-Curricular, Leadership & Voluntary Activies":
        cca()
    if page == "Hobbies & Personal Life":
        hobbies()

if __name__ == "__main__":
    main()