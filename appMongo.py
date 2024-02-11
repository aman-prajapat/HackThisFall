import streamlit as st
from backendMongo import create_user, authenticate_user, search_users
import pymongo
from bson import ObjectId

# your_connection_string
# your_database_name
# Remove Streamlit footer

custom_css = """
<style>
footer {
    display: none;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Define a function to establish a connection to MongoDB
def create_connection():
    client = pymongo.MongoClient("mongodb+srv://monishkanungo23:monish23@@speakersphereclustor.71zohp6.mongodb.net/")  # Replace "your_connection_string" with your MongoDB connection string
    db = client["speakersphere"]  # Replace "your_database_name" with your MongoDB database name
    return db

# Function to complete user details
def complete_details(username, new_password):
    st.header("Speaker Details")
    speaker_name = st.text_input("Speaker Name", value="", placeholder=None)
    domain = st.text_area("Speaker Bio", value="", placeholder=None)
    rating = st.text_input("LinkedIn Link", value="", placeholder=None)
    expertise = st.text_input("Twitter Link", value="", placeholder=None)
    mobile = st.text_input("GitHub Link", value="", placeholder=None)

    if st.button("Submit"):
        # Create a connection to MongoDB
        db = create_connection()
        # Create user with provided details
        create_user(db,speaker_name,domain,rating,expertise, mobile)

st.title("SpeakerSphere")

# Toggle Menu Navigation Bar
st.sidebar.title("Navigation")
menu_options = ["Home", "Login", "Signup", "Find"]
selected_menu_item = st.sidebar.radio("Home", menu_options)

# Display selected section based on the menu item
if selected_menu_item == "Home":
    st.subheader("Welcome to the Home Page!")
    st.write("This is the home page of the application.")
    # Add title and introductory text
    st.title("Welcome to SpeakerSphere!")
    st.write("Connect with speakers and mentors around the globe.")

    # Add sections with more information
    st.header("What is SpeakerSphere?")
    st.write("SpeakerSphere is a platform designed to help you find speakers and mentors in various fields, including technology, business, science, and more.")

    st.header("Why SpeakerSphere?")
    st.write("Whether you're looking for guidance, inspiration, or collaboration, SpeakerSphere connects you with experienced professionals who can help you achieve your goals.")

    st.header("Get Started")
    st.write("Join SpeakerSphere today to start exploring, connecting, and learning!")

    # Add a call-to-action button for signup
    if st.button("Join SpeakerSphere"):
        st.write("Sign up for an account to get started!")

elif selected_menu_item == "Login":
    st.header("Login")
    username_input = st.text_input("Username", value="", placeholder=None)
    password_input = st.text_input("Password", type="password", value="", placeholder=None)
    if st.button("Login"):
        if True:
            st.success("Logged in successfully!")
        else:
            st.error("Invalid username or password.")

elif selected_menu_item == "Signup":
    st.header("Signup")
    new_username = st.text_input("Choose a username", value="", placeholder=None)
    new_password = st.text_input("Choose a password", type="password", value="", placeholder=None)
    complete_details(new_username, new_password)

elif selected_menu_item == "Find":
    st.header("Search Speakers/Mentors")
    search_query = st.text_input("Enter the name of the speaker or mentor or just click search:")
    if st.button("Find"):
        search_results = (search_query)
        if search_results:
            st.write("Search Results:")
            # Display modified results
            st.table(search_results)
        else:
            st.write("No results found.")
