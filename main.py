from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
import requests
# from order_stages import OrderStages
from food_db import get_cuisines, get_dishes
# from fuzzywuzzy import process
import emoji

app = Flask(__name__)
app.secret_key = "secret key thingie"

callers = {
    "+12513001169": "Jack",
    "+12349013030": "Finn",
    "+12348134522": "Chewy",
}

@app.route('/cheers', methods=['GET', 'POST'])
def cheers():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    

    message_options = ['cheers']
    if incoming_msg in message_options:
        hello = "Congrats, now you're a Cheers Insider! We make it simple and easy to find food you'll love. We're so excited to show you what we're building. Save our vCard and you'll recieve exclusive updates from this number. Cheers!"

        msg.body(hello)
        msg.media("https://drive.google.com/uc?export=download&id=104uiuRxIQ5DPS2wIWu62EZS3BjGupPnq")
        responded = True
        print(msg)
        return str(resp)

    else:
        msg.body("Hello and thank you for texting Cheers! I'm not sure what you said there. If you'd like our vCard, just text \"Cheers\" or \"Food\".")
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

if __name__ == '__main__':
    app.run(debug=True)