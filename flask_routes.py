from flask import Flask
from datetime import datetime


app = Flask(__name__)

@app.route('/')
def home():
    return {
        'data': 'Hello Flask'
    }

@app.route('/current_datetime')
def current_datetime():

    moment = datetime.now()

    formatted_time = moment.strftime("%d/%m/%Y %H:%M:%S %p")

    def define_message():
        if moment.hour in range(0,12):
            return 'Bom dia!'
        elif moment.hour in range(13, 18):
            return 'Boa tarde!'
        return 'Boa noite!'

    message = define_message()

    return {
        'current_datetime': formatted_time,
        'message': message
    }