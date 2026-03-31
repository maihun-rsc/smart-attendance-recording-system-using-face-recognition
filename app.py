import streamlit as st  # Streamlit library for building web apps in Python

# Import libraries for data manipulation (pandas) and time-related functions (time, datetime)
import pandas as pd
import time
from datetime import datetime

# Get the current timestamp for calculations
ts = time.time()

# Convert timestamp to human-readable format for date (YYYY-MM-DD)
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")

# Convert timestamp to human-readable format for time (HH:MM-SS)
timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")

# Import the custom function for refreshing the Streamlit app at intervals
from streamlit_autorefresh import st_autorefresh

# Define the refresh interval (2 seconds) and maximum number of refreshes (100)
# This controls how often the app updates the displayed information
count = st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")

# Display a message based on the count value using conditional statements
if count == 0:
  st.write("Count is zero")
elif count % 3 == 0 and count % 5 == 0:
  st.write("FizzBuzz")  # Display "FizzBuzz" if count is divisible by both 3 and 5
elif count % 3 == 0:
  st.write("Fizz")  # Display "Fizz" if count is divisible by 3
elif count % 5 == 0:
  st.write("Buzz")  # Display "Buzz" if count is divisible by 5
else:
  st.write(f"Count: {count}")  # Display the current count value

# Read the attendance data for the current date from a CSV file
df = pd.read_csv("Attendance/Attendance_" + date + ".csv")

# Display the attendance data as a formatted table using Streamlit
st.dataframe(df.style.highlight_max(axis=0))