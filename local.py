
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import streamlit as st


# Define scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Load credentials and authorize
creds = ServiceAccountCredentials.from_json_keyfile_name("service-account.json", scope)
client = gspread.authorize(creds)



# Open the Google Sheet (by name or URL)
spreadsheet = client.open("Amrutha Always Cancels")
sheet = spreadsheet.sheet1  # You can also use .worksheet("Sheet2") if needed



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


