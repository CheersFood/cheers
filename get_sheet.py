import gspread
from oauth2client.service_account import ServiceAccountCredentials

def load(sheet_name):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('cheerskeys.json', scope)

    client = gspread.authorize(creds)

    sheet = client.open(sheet_name)

    return sheet