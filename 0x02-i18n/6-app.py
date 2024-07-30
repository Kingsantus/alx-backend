#!/usr/bin/env python3

"""
6-app.py

A basic Flask app that create a single / route and an index.html template that simply outputs “Welcome to Holberton” as page title and “Hello world” as header.
it initializes Babel for internationalization.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Optional, Dict

class Config:
    """
    Config class defined the available languages and Babel configurations.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(user_id: int) -> Optional[Dict]:
    """
    Retrieve a user dictionary by ID.

    :param user_id: The user ID.
    :return: The user dictionary or None if not found.
    """
    return users.get(user_id)

@app.before_request
def before_request() -> None:
    """
    Function to be executed before each request.
    Sets the user in the global context if the 'login_as' parameter is provided.
    """
    user_id = request.args.get('login_as')
    if user_id is not None:
        g.user = get_user(int(user_id))
    else:
        g.user = None

@babel.localeselector
def get_locale() -> str:
    """
    Finds the best match with our supported languages or use the
    'locale' parameter from the request if present and valid.
    1. Locale from URL parameters
    2. Locale from user settings
    3. Locale from request headers
    4. Default locale

    :return: best matched language or the language from the 'locale' parameter.
    """
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index() -> str:
    """
    Render index.html template.

    Return: The rendered 6-index.html template.
    """
    return render_template('6-index.html', home_title=_("home_title"), home_header=_("home_header")), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
