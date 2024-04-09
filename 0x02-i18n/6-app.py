#!/usr/bin/env python3
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

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

@babel.localeselector
def get_locale():
    # 1. Check for locale from URL parameters
    if 'locale' in request.args:
        requested_locale = request.args.get('locale')
        if requested_locale in app.config['LANGUAGES']:
            return requested_locale

    # 2. Check for locale from user settings
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    # 3. Check for locale from request header
    accept_languages = request.accept_languages
    for lang in accept_languages:
        if lang in app.config['LANGUAGES']:
            return lang

    # 4. Default locale
    return app.config['BABEL_DEFAULT_LOCALE']

@app.route('/')
def index():
    return render_template('6-index.html')

if __name__ == '__main__':
    app.run()
