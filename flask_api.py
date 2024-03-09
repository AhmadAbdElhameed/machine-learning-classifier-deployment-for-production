# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, request


app = Flask(__name__)

@app.route('/',methods = ['POST'])


def add():
    a = request.form["a"]
    b = request.form["b"]
    return str(int(a)+int(b))




if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)