#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    # Check if the 'locale' parameter is present in the request
    if 'locale' in request.args:
        requested_locale = request.args.get('locale')
        # Check if the requested locale is supported
        if requested_locale in app.config['LANGUAGES']:
            return requested_locale

    # If 'locale' parameter is not present or not supported, resort to default behavior
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    return render_template('4-index.html')

if __name__ == '__main__':
    app.run()
