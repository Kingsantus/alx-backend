#!/usr/bin/env python3

"""
1-app.py

A basic Flask app that create a single / route and an index.html template that simply outputs “Welcome to Holberton” as page title and “Hello world” as header.
it initializes Babel for internationalization.
"""

from flask import Flask, render_template
from flask_babel import Babel

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

@app.route('/')
def index() -> str:
    """
    Render index.html template.

    Return: The rendered 1-index.html template.
    """
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
