#!/usr/bin/env python3

"""
0-app.py

A basic Flask app that create a single / route and an index.html template that simply outputs “Welcome to Holberton” as page title and “Hello world” as header.

"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home() -> str:
    """
    Render index.html template.

    :return: The rendered 0-index.html template.
    """
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
