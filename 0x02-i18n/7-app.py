#!/usr/bin/env python3
"""7-app.py"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz

app = Flask(__name__)
babel = Babel(app)

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
def get_timezozne():
    """timezone"""
    if 'timezone' in request.args:
        requested_timezone = request.args.get('timezone')
        try:
            pytz.timezone(requested_timezone)
            return requested_timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    if g.user and g.user['timezone']:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    return 'UTC'

@app.route('/')
def index():
    return render_template('7-index.html')

if __name__ == '__main__':
    app.run()
