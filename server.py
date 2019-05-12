#!/usr/bin/python
# -*- coding: utf-8-*-
from flask import Flask, request

app = Flask(__name__)
@app.route("/")
def func():
    return 'Rtn:{}'.format(request.args.get('param'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9999)
