import streamlit as st
import gspread
from google.oauth2 import service_account

# Set up Google Sheets API
service_account_info = st.secrets["gcp_service_account"]
scopes = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
creds = service_account.Credentials.from_service_account_info(service_account_info, scopes=scopes)
client = gspread.authorize(creds)


def save_feedback(name, email, feedback):
    # Open the Google Sheets spreadsheet
    spreadsheet = client.open(
        "Article Mind - User Feedbacks"
    )  # Replace with your spreadsheet name
    sheet = spreadsheet.get_worksheet(0)  # Use the first worksheet

    # Append data to the spreadsheet
    data = [name, email, feedback]
    sheet.append_row(data)
