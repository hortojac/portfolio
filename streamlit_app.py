import streamlit as st
from streamlit_extras.buy_me_a_coffee import button
import requests
import time

# Streamlit Page Configuration
st.set_page_config(
    page_title="Jacob Horton's Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None
)

# Page Title
st.title("Hello, I'm Jacob Horton :wave:")

# Page Columns
column1, spacer, column2 = st.columns([5, 0.5, 5])

with column1:
    st.header("About Me", divider="gray")
    st.write("I'm a computer science student at the University of Kansas. I've been immersing myself in data science and machine learning, with a keen interest in the innovative field of generative AI.")

    # Custom CSS for the link buttons
    st.markdown("""
        <style>
            .row-widget.stLinkButton a {
                background-color: #FFDD00;
                color: #000000;
            }
            .row-widget.stLinkButton a:hover {
                background-color: #808080;
                color: #FFFFFF;
            }
        </style>
        """, unsafe_allow_html=True)

    button_column1, button_column2, button_column3 = st.columns(3)

    with button_column1:
        st.link_button(":page_facing_up: Resume", "https://drive.google.com/file/d/1MJ7M5TDZ3MNY9TDAB46xR0BzlyTChMO-/view?usp=sharing", use_container_width=True)
    with button_column2:
        st.link_button(":desktop_computer: GitHub", "https://github.com/hortojac", use_container_width=True)
    with button_column3:
        st.link_button(":necktie: LinkedIn", "https://www.linkedin.com/in/jacobleehorton/", use_container_width=True)

    # Initialize session state variables
    if 'name' not in st.session_state:
        st.session_state['name'] = ''
    if 'email' not in st.session_state:
        st.session_state['email'] = ''
    if 'message' not in st.session_state:
        st.session_state['message'] = ''

    st.header("Contact Me", divider="gray")

    # Use session state for input values
    name = st.text_input("Name", value=st.session_state['name'], placeholder="Your Name")
    email = st.text_input("Email", value=st.session_state['email'], placeholder="Your Email")
    message = st.text_area("Message", value=st.session_state['message'], placeholder="Your Message")

    # Custom CSS for the send button
    st.markdown("""
        <style>
            div.stButton > button:first-child {
                background-color: #FFDD00;
                color: #000000;
            }
            div.stButton > button:first-child:hover {
                background-color: #808080;
                color: #FFFFFF;
            }
        </style>
        """, unsafe_allow_html=True)
    send_column1, send_column2, send_column3 = st.columns([2, 0.5, 2])
    with send_column1:
        submit_button = st.button(":e-mail: Send Message", use_container_width=True)
    with send_column2:
        pass
    with send_column3:
        st.link_button(":coffee: Buy Me a Coffee", "https://www.buymeacoffee.com/hortojac", use_container_width=True)

    if submit_button:
        form_data = {
            'entry.1193324939': name,
            'entry.1291554401': email,
            'entry.817569982': message
        }
        response = requests.post('https://docs.google.com/forms/d/e/1FAIpQLSf9HogLCJE0UeLFb7X87OFP-75j6FMzZCw6o4BZG55JUYAEUg/formResponse', data=form_data)

        if response.status_code == 200:
            st.success("Thank you for your message! I'll get back to you soon.")
            # Reset session state (and therefore widget values)
            st.session_state['name'] = ''
            st.session_state['email'] = ''
            st.session_state['message'] = ''

            time.sleep(3)
            # Rerun the app to update the widgets with empty values
            st.experimental_rerun()
        else:
            st.error("An error occurred. Please try again.")

# Spacer Column
with spacer:
    pass

with column2:
    # Projects Section
    st.header("My Projects", divider="gray")

    st.subheader("KU Triangle Chatbot")
    st.write("A chatbot that answers questions about the KU Triangle Fraternity. It was built using LlamaIndex, powered by GPT-3.5, and Streamlit.")
    project1_column1, project1_column2, project1_column3 = st.columns(3)
    with project1_column1:
        st.link_button(":robot_face: View App", "https://st-triangle-chatbot.streamlit.app/", use_container_width=True)
    with project1_column2:
        st.link_button(":file_folder: View Repository", "https://github.com/hortojac/st-triangle-chatbot", use_container_width=True)
    with project1_column3:
        pass

    st.subheader("BillBriefs")
    st.write("BillBriefs is a Streamlit application designed to streamline the understanding of legislative bills. Users begin by inputting their address, upon which the app identifies their represented congressmen and retrieves all bills during these members' tenures. Utilizing GPT-3.5, BillBriefs then condenses these bills into concise, one-line summaries. Users can swipe through these summaries to express support, opposition, or skip them. Finally, the app reveals the alignment of the user's views with those of members up for re-election, offering a clear and personalized insight into legislative representation.")
    project2_column1, project2_column2, project2_column3 = st.columns(3)
    with project2_column1:
        st.link_button(":globe_with_meridians: View Website", "https://billbriefs.com/", use_container_width=True)
    with project2_column2:
        st.link_button(":file_folder: View Repository", "https://github.com/hortojac/billbriefs-streamlit", use_container_width=True)
    with project2_column3:
        pass