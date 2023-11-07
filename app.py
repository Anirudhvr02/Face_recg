import streamlit as st
# from streamlit_lottie import st_lottie
import requests
from datetime import datetime
import pandas as pd
import os
import random

# lottie_face = "https://lottie.host/c8b44339-efbe-4b6c-9537-921efeec632c/T7GyFCnelQ.json"
# lottie_automated = "https://lottie.host/62608296-d173-4d4b-a736-ec5f5007a956/fQtmty0Wee.json"

st.set_page_config(page_title="Face Based Attendance System", layout="wide")

def load(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json

#----------------------------Header---------------------#
with st.container():
    l,r = st.columns(2)
    with l:
        st.title("Face Based Attendance System")
        st.subheader("Overview")
        st.write("The Face Recognition-Based Attendance System is an innovative solution designed to automate the attendance tracking process in various environments, such as educational institutions, corporate offices, and events. Leveraging advanced facial recognition technology, this system eliminates the need for manual attendance management, providing a seamless and accurate alternative.")
    with r:
        # st_lottie(lottie_automated, height=200, key="automated")
        
#---------------------Live attendance display-----------#
# with st.container():
    # st.write("---")
    # left_column,right_column = st.columns(2)
    
    with left_column:
        st.header("Live Capture of Face Attendance")
        st.write("This section displays the comparison of captured image and original image of the employee.")
        # Display current time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.write(f"Current Time: {current_time}")
        # List of names
        names = ["Anirudh", "Venkatesh", "Vinayak", "Gadha", "Sandeep"]
        # Generate a random index
        random_index = random.randint(0, len(names)-1)
        # Get the random name
        random_name = names[random_index]
        # Display the random name
        st.write(f"Employee name: {random_name}")
        print(random)

    with right_column:
        # Add date picker
        selected_date = st.date_input("Select Date", datetime.today())
        # Button to view database for selected date
        if st.button("View Database"):
            # Construct the file name based on the selected date
            file_name = f'./attendance_records/{selected_date.strftime("%Y-%m-%d")}.csv'
            # Check if the file exists
            if os.path.isfile(file_name):
                # Read the CSV file and store it in a DataFrame
                df = pd.read_csv(file_name)  
                st.write(df)  # Visualize the dataframe in the Streamlit app
            else:
                st.write("No records found for the selected date.")

#---------------------to add New_user-------------------#
with st.container():
    st.write("---")
    left_column,right_column = st.columns(2)
    with left_column:
        st.header("Register a new user")
        st.write("Enter the details of the user")
        first_name = st.text_input("First name:")
        last_name = st.text_input("Last name:")
        designation = st.text_input("Designation:")
        
    with right_column:
        # st_lottie(lottie_face, height=200, key="face")
        uploaded_file = st.file_uploader("Upload a picture of the user",type=["jpg", "png", "jpeg"])

# Process uploaded file if any
if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
