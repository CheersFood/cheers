import gspread
# import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('cheerskeys.json', scope)

# authorize the clientsheet 
client = gspread.authorize(creds)

sheet = client.open('Cheers_Insiders_User_Numbers')

# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)

records_data = sheet_instance.get_all_records()

sheet_instance.insert_row(["hello"], 1)
print(records_data)