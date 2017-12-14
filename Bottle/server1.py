#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-13 下午8:07
# @File    : server1.py

from bottle import template, Bottle, static_file, request, redirect
import bottle
from bottle import jinja2_template # jinia2 tpl model ==>Django
bottle.TEMPLATE_PATH.append('./templates/')
root = Bottle()
from gevent import monkey
monkey.patch_all()

@root.route('/login/', method=["POST", "GET"])
def login():
    # return "Hello World"
    # return template('<b>Hello {{name}}</b>!', name="Alex")
    if request.method == "GET":
        return template("login.html")
    else:
        print(request.forms.get("username"))
        print(request.forms.get("password"))
        return redirect("/index/")

@root.route("/sta/<path:path>")
def callback(path):
    return static_file(path, root="static")

def custome():
    return "<h2>hello 12312321</h2>"

@root.route("/index/")
def index():
    user_list = [
        {"id": 1, "age": 28, "name": "tom"},
        {"id": 2, "age": 18, "name": "1tom"},
        {"id": 5, "age": 22, "name": "tom2"},
    ]
    return template("index.html",
                    chm = custome,
                    age="root", name="Bottle", user_list=user_list)
root.run(host='localhost', port=8003, server="gevent")
