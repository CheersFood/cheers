from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import requests
# from order_stages import OrderStages
from food_db import get_cuisines, get_dishes
import get_sheet
import logging
import google.cloud.logging
import os
import time
import http.client

log_client = google.cloud.logging.Client()
log_client.setup_logging()

sheet = get_sheet.load("Cheers_Insiders_User_Numbers")
sheet_instance = sheet.get_worksheet(0)

app = Flask(__name__)
app.secret_key = "secret key thingie"

# callers = {
#     "+12513001169": "Jack",
#     "+12349013030": "Finn",
#     "+12348134522": "Chewy",
# }

@app.route('/cheers', methods=['GET', 'POST'])
def cheers():
    incoming_msg = request.values.get('Body', '').lower()

    # media_files = [(request.POST.get("MediaUrl{}".format(i), ''),
    #                 request.POST.get("MediaContentType{}".format(i), ''))
    #                for i in range(0, num_media)]
    
    print(request.values.get('MediaUrl0', ''))
    print(incoming_msg)
    logging.info("{} texted: {}".format(request.values.get('From'), incoming_msg))
    resp = MessagingResponse()
    msg = resp.message()
    

    new_user_options = ['cheers']
    existing_user_options = ['cheers', 'vcard', 'socials']
    if request.values.get('From') not in sheet_instance.col_values(1):
        sheet_instance.insert_row([request.values.get('From')], 1)
        if incoming_msg in new_user_options:
            hello = "Congrats, now you're a Cheers Insider! We make it simple and easy to find food you'll love. We're so excited to show you what we're building. Save our vCard and you'll recieve exclusive updates from this number. Cheers!"
            
            msg.body(hello)
            msg.media("https://drive.google.com/uc?export=download&id=104uiuRxIQ5DPS2wIWu62EZS3BjGupPnq")
            responded = True
            logging.info("Cheers responded with: {}".format(msg.body))
            print(msg)
            return str(resp)

    elif request.values.get('From') in sheet_instance.col_values(1):
        if incoming_msg in existing_user_options:
            hello = "Hi! Welcome back to Cheers Insiders! Check out our vCard for all our contact info. Cheers!"
            
            msg.body(hello)
            msg.media("https://drive.google.com/uc?export=download&id=104uiuRxIQ5DPS2wIWu62EZS3BjGupPnq")
            responded = True
            print(msg)
            return str(resp)

    # elif request.values.get('MediaUrl0', '') == True:
    #     print("Picture!")
    #     msg.body("Picture!")
    #     responded = True
    #     return str(resp)

    else:
        msg.body("Hello and thank you for texting Cheers Insiders! I'm not sure what you said there. If you'd like our vCard, just text \"Cheers\"")
        logging.info("Cheers responded with: {}".format(msg.body))
        responded = True
        return str(resp)

    # incoming_msg = request.values.get('Body', '').lower()
    # resp = MessagingResponse()
    # msg = resp.message()


    # # msg.media(image_url)
    # # counter = session.get('counter', 0)
    # # counter += 1
    # # session['counter'] = counter
    # # print(counter)
    # responded = False
    # options = ["1", "2", "3", "4", "5", "1.", "2,", "3.", "4.", "5."]
    # cuisines = get_cuisines()
    # if "food" in incoming_msg:
        
    #     # msg.media("https://drive.google.com/uc?export=download&id=1NjZDEH6QIfKELPv0_XMCCGDJLH1nxe-r")
        
    #     welcome = "Welcome to Cheers! What cuisine would you like?\n1. {0}\n2. {1}\n3. {2}\n4. {3}\n5. {4}".format(cuisines[0], cuisines[1], cuisines[2], cuisines[3], cuisines[4])
    #     msg.body(welcome)
    #     responded = True
    #     # session.clear()
    #     # print(counter)
    #     return str(resp)

    # if incoming_msg in options:
    #     # if counter == 2:
    #     print(incoming_msg)
    #     print(cuisines)
    #     choice = cuisines[int(incoming_msg) - 1]
    #     print(choice)
    #     dishes = get_dishes(str(choice))
    #     print(dishes)
    #     dishes2 = "Great! Here are some fun dishes.\n1. {0}\n2. {1}".format(dishes[0], dishes[1])
    #     msg.body(dishes2)
    #     return str(resp)

    # else:
    #     print(incoming_msg)

    # """Respond with the number of text messages sent between two parties."""
    # # Increment the counter
    # counter = session.get('counter', 0)
    # counter += 1

    # # Save the new counter value in the session
    # session['counter'] = counter
    # print(request.values)
    # from_number = request.values.get('From')
    # if from_number in callers:
    #     name = callers[from_number]
    # else:
    #     name = "Friend"

    # # Build our reply
    # message = '{} has messaged {} {} times.' \
    # .format(name, request.values.get('To'), counter)

    # # Put it in a TwiML response
    # resp = MessagingResponse()
    # resp.message(message)

    # return str(resp)

@app.route('/')
def hello():
    return '<h1> Hello World!!! I build automatically now!! Woohoo! </h1>'

@app.route('/mass_text', methods=['GET', 'POST'])
def mass_text():
    # sheet2 = get_sheet.load("Lunch_Numbers_Switch")
    # sheet_instance2 = sheet2.get_worksheet(0)

    # sheet2 = get_sheet.load("Lunch_Numbers_Switch")
    # sheet_instance2 = sheet2.get_worksheet(0)

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    # numbers = sheet_instance2.col_values(3)[1:]

    operators = ['+12054824656']
    numbers = ['+12513001169', '+12516043287']
    mass_text = ""

    incoming_msg = request.values.get('Body', '').lower()
    incoming_pic = request.values.get('MediaUrl0', '')
    from_number = request.values.get('From')
    mass_text_start = False
    # request.values.has_key('MediaUrl0')
    print(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()

    # The below code executes if the operator has sent out a new mass-text
    if from_number in operators:
        mass_text_start = True
        logging.info("A new Innovation Depot/Hardware Park mass text session has been created from {}".format(from_number))
        print("New message from operator detected")
        print(incoming_pic)
        # sheet_instance2.insert_row([request.values.get('From')], 1)
        
        if mass_text_start == True:
            if incoming_pic != '':
                # Mass text operator would like to send is stored as 'mass-text' and sent to list of numbers from excel spreadsheet
                mass_text = incoming_msg
                for number in numbers:
                    conn = http.client.HTTPSConnection('enf42zlvj3y3890.m.pipedream.net')
                    print(conn)
                    time.sleep(15)
                    message = client.messages.create(
                            to=number, 
                            from_="+12052725540", 
                            body=mass_text, 
                            media_url=[incoming_pic],
                            status_callback="https://enf42zlvj3y3890.m.pipedream.net")
                    logging.info("Successfully texted {} to {}".format(message, str(number)))
                    print(message)
                    print(number)

                logging.info("Text was sent to {} numbers".format(len(numbers)))

                # Response to operator
                msg.body("Your mass-text has been sent. All responses will appear in this chat window.")

                responded = True
                print(msg)
                return str(resp)

            elif incoming_pic == '':
                    # Mass text operator would like to send is stored as 'mass-text' and sent to list of numbers from excel spreadsheet
                mass_text = incoming_msg
                for number in numbers:
                    time.sleep(15)
                    message = client.messages.create(
                            to=number, 
                            from_="+12052725540", 
                            body=mass_text, 
                            media_url=[incoming_pic],
                            status_callback='https://enf42zlvj3y3890.m.pipedream.net')
                    logging.info("Successfully texted {} to {}".format(message, str(number)))
                    print(message)
                    print(number)

                logging.info("Text was sent to {} numbers".format(len(numbers)))

                # Response to operator
                msg.body("Your mass-text has been sent. All responses will appear in this chat window.")

                responded = True
                print(msg)
                return str(resp)
    
    # The below code executes if a customer is responding to a mass-text
    elif from_number not in operators:
        logging.info("{} has responded to mass-text with {}".format(from_number, incoming_msg))
        print("User has responded to mass-text with {}".format(incoming_msg))
        conn = http.client.HTTPSConnection('enf42zlvj3y3890.m.pipedream.net')
        print(conn)

        new_body = "{}: {}".format(from_number, incoming_msg)
        print(new_body)
        # Customer response is sent to operator
        message = client.messages.create(
                to="+12054824656", 
                from_="+12052725540", 
                body=new_body,
                status_callback='https://enf42zlvj3y3890.m.pipedream.net'
        )

        logging.info("Successfully delivered customer repsonse to operator.")
        return "Successfully delivered customer repsonse to operator."

if __name__ == '__main__':
    app.run(debug=True)