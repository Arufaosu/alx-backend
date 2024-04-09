#!/usr/bin/env python3
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
import pytz
from datetime import datetime

app = Flask(__name__)
babel = Babel(app)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(user_id):
    return users.get(user_id)

@app.before_request
def before_request():
    login_as = request.args.get('login_as')
    g.user = get_user(int(login_as)) if login_as else None

@babel.timezoneselector
def get_timezone():
    # Logic to get the timezone...

@app.route('/')
def index():
    current_time = datetime.now(pytz.timezone(get_timezone()))
    formatted_time = current_time.strftime('%b %d, %Y, %I:%M:%S %p')  # Default format

    return render_template('index.html', current_time=formatted_time)

if __name__ == '__main__':
    app.run()
