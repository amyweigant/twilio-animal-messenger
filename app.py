#!/usr/bin/env python
from flask import Flask
from flask import request
from twilio import twiml
app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms():
    response = twiml.Response()
    body = request.form['Body']

    if "cat" in body.lower():
        image = "http://cattowngame.com/images/cat.jpg"
        text = "a nice cat"
    elif "emu" in body.lower():
        image = "http://cattowngame.com/images/emu.jpg"
        text = "a curious emu"
    elif "dog" in body.lower():
        image = "http://cattowngame.com/images/dog.jpg"
        text = "a happy dog"
    else:
        image = "http://cattowngame.com/images/questionmark.jpg"
        text = "something else. Try replying with the words 'dog', 'cat', or 'emu'"

    with response.message() as message:
        message.body = "You seem to want {0}.".format(text)
        message.media(image)
    return str(response)


if __name__ == "__main__":
    app.run()
