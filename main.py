from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
import requests
# from order_stages import OrderStages
from food_db import get_cuisines, get_dishes

app = Flask(__name__)
app.secret_key = "secret key thingie"

@app.route('/cheers', methods=['POST'])
def cheers():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    # msg.media(image_url)
    # counter = session.get('counter', 0)
    # counter += 1
    # session['counter'] = counter
    # print(counter)
    responded = False
    options = ["1", "2", "3", "4", "5", "1.", "2,", "3.", "4.", "5."]
    cuisines = get_cuisines()
    if "food" in incoming_msg:
        
        msg.media("https://drive.google.com/uc?export=download&id=1NjZDEH6QIfKELPv0_XMCCGDJLH1nxe-r")
        
        # welcome = "Welcome to Cheers! What cuisine would you like?\n1. {0}\n2. {1}\n3. {2}\n4. {3}\n5. {4}".format(cuisines[0], cuisines[1], cuisines[2], cuisines[3], cuisines[4])
        # msg.body(welcome)
        responded = True
        # session.clear()
        # print(counter)
        return str(resp)

    if incoming_msg in options:
        # if counter == 2:
        print(incoming_msg)
        print(cuisines)
        choice = cuisines[int(incoming_msg) - 1]
        print(choice)
        dishes = get_dishes(str(choice))
        print(dishes)
        dishes2 = "Great! Here are some fun dishes.\n1. {0}\n2. {1}".format(dishes[0], dishes[1])
        msg.body(dishes2)
        return str(resp)

    else:
        print(incoming_msg)


@app.route('/')
def hello():
    return '<h1> Hello World!!! I build automatically now! </h1>'

if __name__ == '__main__':
    app.run(debug=True)