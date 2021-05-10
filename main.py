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
from http import client

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

    sheet = get_sheet.load("Mass_Text_Test")
    sheet_instance = sheet.get_worksheet(0)

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    twil_client = Client(account_sid, auth_token)

    # numbers = ['+12513338432', '+12516043287', '+14149090265', '+12513001169']

    numbers = sheet_instance.col_values(1)
    names = sheet_instance.col_values(2)

    operator = ['+12516043287']

    conn = client.HTTPSConnection('enf42zlvj3y3890.m.pipedream.net')
    
    incoming_msg = request.values.get('Body', '')
    incoming_pic = request.values.get('MediaUrl0', '')
    from_number = request.values.get('From')
    
    mass_text_start = False

    resp = MessagingResponse()
    msg = resp.message()

    if from_number in operator:

        mass_text_start = True

        if mass_text_start == True:

            if request.values.has_key('MediaUrl0'):

                logging.info("New image-based mass-text session has been started.")

                for number in numbers:
                    print(number)
                    message = twil_client.messages.create(
                            to=number, 
                            from_="+12052725540",
                            body=incoming_msg,
                            media_url=[incoming_pic],
                            status_callback="https://enf42zlvj3y3890.m.pipedream.net")
                    
                    logging.info("Successfully texted {} to {}".format(incoming_msg, str(number)))
                    print("Successfully texted {} to {}".format(incoming_msg, str(number)))

                logging.info("Text was sent to {} numbers".format(len(numbers)))
                print("Text was sent to {} numbers".format(len(numbers)))

                msg.body("Your mass-text has been sent. All responses will appear in this chat window.")

                responded = True
                print(msg)
                return str(resp)

            elif not request.values.has_key('MediaUrl0'):
                logging.info("New mass-text session has been started.")
                for number in numbers:
                    message = twil_client.messages.create(
                            to=number, 
                            from_="+12052725540",
                            body=incoming_msg,
                            status_callback="https://enf42zlvj3y3890.m.pipedream.net")
                    
                    logging.info("Successfully texted {} to {}".format(incoming_msg, str(number)))
                    print("Successfully texted {} to {}".format(incoming_msg, str(number)))

                logging.info("Text was sent to {} numbers".format(len(numbers)))
                print("Text was sent to {} numbers".format(len(numbers)))

                msg.body("Your mass-text has been sent. All responses will appear in this chat window.")

                responded = True
                print(msg)
                return str(resp)

    elif from_number not in operator:
        name_vals = [numbers.index(val) for val in numbers if val == from_number]
        name = names[name_vals[0]]

        logging.info("{} has responded to mass-text with {}".format(name, incoming_msg))
        print("{} has responded to mass-text with {}".format(name, incoming_msg))

        new_body = "{}: {}".format(name, incoming_msg)

        print(new_body)

        # Customer response is sent to operator
        message = twil_client.messages.create(
                to="+12516043287", 
                from_='+12052725540', 
                body=new_body,
                status_callback='https://enf42zlvj3y3890.m.pipedream.net'
        )

        logging.info("Successfully delivered customer repsonse to operator.")
        print("Successfully delivered customer repsonse to operator.")

        return "Successfully delivered customer repsonse to operator."


if __name__ == '__main__':
    app.run(debug=True)