import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set up Google Sheets API
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
creds = ServiceAccountCredentials.from_json_keyfile_name("google_creds.json", scope)
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