#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-14 下午4:03
# @Author  : Gavin Gan
# @Site    : 
# @File    : flask-MiddleWare.py
# @Software: PyCharm
from flask import Flask

app = Flask(__name__)

@app.route("/index/")
def home():
    return "hello"


def my_wsgi_app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [bytes('<h1>Hello, web!</h1>', encoding='utf-8'), ]

class Foo:
    def __init__(self, w):
        self.w = w
    def __call__(self, *args, **kwargs):
        # environ, start_response
        print("middle")
        return self.w(*args, **kwargs)

if __name__ == "__main__":
    app.wsgi_app = Foo(app.wsgi_app)
    app.run(port=8004)