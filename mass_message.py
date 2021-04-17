import os
from twilio.rest import Client
import requests
import get_sheet
import google.cloud.logging
import logging

logClient = google.cloud.logging.Client()
logClient.setup_logging()

sheet = get_sheet.load("Cheers_Insiders_User_Numbers")
sheet_instance = sheet.get_worksheet(0)

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

#DO NOT UNCOMMENT THE BELOW CODE UNLESS YOU ARE SENDING MASS MESSAGES!!!!!
# numbers = sheet_instance.col_values(1)

# text = "Cheers and Happy Friday! In case you missed the news, Cheers won second place at Innovation Depot's Voltage Pitch-Off!! For more Cheers, feel free to follow us on Instagram at @textcheers!"

# for number in numbers:
#     print(number)
#     message = client.messages.create(
#             to=number, 
#             from_="+12052256976", 
#             body=text)
#     logging.info("Successfully texted {}".format(str(number)))
