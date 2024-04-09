#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babel import Babel, _
from flask_babel import gettext

app = Flask(__name__)
babel = Babel(app)

class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    return render_template('1-index.html')

@app.route('/set_language', methods=['POST'])
def set_language():
    lang = request.form['language']
    if lang in app.config['LANGUAGES']:
        session['language'] = lang
    return redirect(request.referrer or url_for('index'))

if __name__ == '__main__':
    app.run()
