# from flask import Flask, request, session
# from twilio.twiml.messaging_response import MessagingResponse
# import os
# from twilio.rest import Client
# import requests
# import get_sheet
# import google.cloud.logging
# import logging
# from http import client

# app = Flask(__name__)
# app.secret_key = "secret key thingie"

# logClient = google.cloud.logging.Client()
# logClient.setup_logging()

# @app.route('/mass_text', methods=['GET', 'POST'])
# def mass_text():

#     sheet = get_sheet.load("Mass_Text_Test")
#     sheet_instance = sheet.get_worksheet(0)

#     account_sid = os.environ['TWILIO_ACCOUNT_SID']
#     auth_token = os.environ['TWILIO_AUTH_TOKEN']
#     twil_client = Client(account_sid, auth_token)

#     # numbers = ['+12513338432', '+12516043287', '+14149090265', '+12513001169']

#     numbers = sheet_instance.col_values(1)
#     names = sheet_instance.col_values(2)

#     operator = ['+12516043287']

#     conn = client.HTTPSConnection('enf42zlvj3y3890.m.pipedream.net')
    
#     incoming_msg = request.values.get('Body', '')
#     incoming_pic = request.values.get('MediaUrl0', '')
#     from_number = request.values.get('From')
    
#     mass_text_start = False

#     resp = MessagingResponse()
#     msg = resp.message()

#     if from_number in operator:

#         mass_text_start = True

#         if mass_text_start == True:

#             if request.values.has_key('MediaUrl0'):

#                 logging.info("New image-based mass-text session has been started.")

#                 for number in numbers:
#                     print(number)
#                     message = twil_client.messages.create(
#                             to=number, 
#                             from_="+18478071592",
#                             body=incoming_msg,
#                             media_url=[incoming_pic],
#                             status_callback="https://enf42zlvj3y3890.m.pipedream.net")
                    
#                     logging.info("Successfully texted {} to {}".format(incoming_msg, str(number)))
#                     print("Successfully texted {} to {}".format(incoming_msg, str(number)))

#                 logging.info("Text was sent to {} numbers".format(len(numbers)))
#                 print("Text was sent to {} numbers".format(len(numbers)))

#                 msg.body("Your mass-text has been sent. All responses will appear in this chat window.")

#                 responded = True
#                 print(msg)
#                 return str(resp)

#             elif not request.values.has_key('MediaUrl0'):
#                 logging.info("New mass-text session has been started.")
#                 for number in numbers:
#                     message = twil_client.messages.create(
#                             to=number, 
#                             from_="+18478071592",
#                             body=incoming_msg,
#                             status_callback="https://enf42zlvj3y3890.m.pipedream.net")
                    
#                     logging.info("Successfully texted {} to {}".format(incoming_msg, str(number)))
#                     print("Successfully texted {} to {}".format(incoming_msg, str(number)))

#                 logging.info("Text was sent to {} numbers".format(len(numbers)))
#                 print("Text was sent to {} numbers".format(len(numbers)))

#                 msg.body("Your mass-text has been sent. All responses will appear in this chat window.")

#                 responded = True
#                 print(msg)
#                 return str(resp)

#     elif from_number not in operator:
#         name_vals = [numbers.index(val) for val in numbers if val == from_number]
#         name = names[name_vals[0]]

#         logging.info("{} has responded to mass-text with {}".format(name, incoming_msg))
#         print("{} has responded to mass-text with {}".format(name, incoming_msg))

#         new_body = "{}: {}".format(name, incoming_msg)

#         print(new_body)

#         # Customer response is sent to operator
#         message = twil_client.messages.create(
#                 to="+12516043287", 
#                 from_='+18478071592', 
#                 body=new_body,
#                 status_callback='https://enf42zlvj3y3890.m.pipedream.net'
#         )

#         logging.info("Successfully delivered customer repsonse to operator.")
#         print("Successfully delivered customer repsonse to operator.")

#         return "Successfully delivered customer repsonse to operator."

# if __name__ == '__main__':
#     app.run(debug=True)