from googleapiclient.discovery import build
from google.oauth2 import service_account
import random

SERVICE_ACCOUNT_FILE = 'cheerskeys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)



# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '10Qmo3SIVTmg8Bz86SGKOLusfKpRm3Ef2tsW63juDpY0'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range="Menu!A1:K137").execute()

def get_cuisines():
        cuisines_rep = []
        for i in range(0, len(result.get('values'))):
                cuisines_rep.append(result.get('values')[i][0])
                
        cuisines_rep.remove("Category")

        cuisines = []

        [cuisines.append(x) for x in cuisines_rep if x not in cuisines]

        list_of_five = random.sample(cuisines, 5)
        return list_of_five

def get_dishes(selection):
        print(selection)
        dishes = []
        counter = 1
        for i in range(0, len(result.get('values'))):
                if result.get('values')[i][0] == selection:
                        if counter != 7:
                                dishes.append(result.get('values')[i])
                                counter+=1
        
        item1 = [dishes[0][1], dishes[0][2]]
        item2 = [dishes[1][1], dishes[1][2]]
        item3 = [dishes[2][1], dishes[2][2]]
        item4 = [dishes[3][1], dishes[3][2]]
        # item5 = [dishes[4][1], dishes[4][2], dishes[4][9]]

        new_dishes = [item1, item2]
        return new_dishes
        


