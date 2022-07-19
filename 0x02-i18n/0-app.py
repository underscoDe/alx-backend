#!/usr/bin/env python3
""" basic Flask application
"""
from flask import (
    Flask,
    render_template
)


app = Flask(__name__)


@app.route('/')
def index():
    """ return a hello world page
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
