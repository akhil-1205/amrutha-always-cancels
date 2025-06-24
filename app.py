import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import streamlit as st
import json
import os

with open("service-account.json", "w") as f:
    f.write(os.getenv("GOOGLE_CREDS_JSON"))

# Define scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Load credentials and authorize
creds = ServiceAccountCredentials.from_json_keyfile_name("service-account.json", scope)
client = gspread.authorize(creds)


# Open the Google Sheet
spreadsheet = client.open("Amrutha Always Cancels")
sheet = spreadsheet.sheet1  


# Get all rows as raw data
rows = sheet.get_all_values()

# Check the header (row 0)
raw_headers = rows[0]
print(raw_headers)

# Fix duplicates or empty strings
headers = [f"Column_{i}" if h.strip() == "" else h for i, h in enumerate(raw_headers)]

# Create DataFrame from remaining rows
df = pd.DataFrame(rows[1:], columns=headers)
df.head()



st.title("Amrutha Always Cancels")

# Show each row individually
for idx, row in df.iterrows():
    st.subheader(f"Event {idx + 1}: {row['What event did she cancel?']}")
    #st.write(f"🕒 **Timestamp**: `{row['Timestamp']}`")
    st.write(f"📅 **Event Date**: `{row['When was the event?']}`")
    st.write(f"💬 **Excuse**: *{row['What was her \"excuse\"?']}*`")
    st.markdown("---")  # horizontal separator between entries

# Add form link section
st.markdown("## Are you a victim too? You are not alone!")
st.markdown("### [Click here to report a new cancellation](https://forms.gle/XRzjKL8kS692WyFm7)", unsafe_allow_html=True)




