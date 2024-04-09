#!/usr/bin/env python3
"""4-app.py"""
from typing import Union
from flask import Flask, request
from flask_babel import Babel
from config import Config
from routes.routes_4 import app_routes


class Config(object):
    """config class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)
babel = Babel(app)

app.config.from_object(Config)

@babel.localeselector
def get_locale() -> Union[str, None]:
    """union"""
    localeReq = request.args['locale']
    if localeReq in app.config['LANGUAGES']:
        return localeReq
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False))
def index() -> str:
    return render_template('4-index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
