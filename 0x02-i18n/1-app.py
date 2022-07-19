#!/usr/bin/env python3
""" Basic Babel setup
"""
from flask import (
    Flask,
    render_template
)
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)
Config = __import__('configs').Config


app.config.from_object(Config)


@app.route('/')
def index():
    """ return a hello world page
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
