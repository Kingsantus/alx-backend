#!/usr/bin/env python3

"""
4-app.py

A basic Flask app that create a single / route and an index.html template that simply outputs “Welcome to Holberton” as page title and “Hello world” as header.
it initializes Babel for internationalization.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

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

@babel.localeselector
def get_locale() -> str:
    """
    Finds the best match with our supported languages or use the
    'locale' parameter from the request if present and valid.

    :return: best matched language or the language from the 'locale' parameter.
    """

    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index() -> str:
    """
    Render index.html template.

    Return: The rendered 4-index.html template.
    """
    return render_template('4-index.html', home_title=_("home_title"), home_header=_("home_header")), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
