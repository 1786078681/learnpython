#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-14 上午9:34
# @Author  : Gavin Gan
# @Site    : 
# @File    : reserver.py
# @Software: PyCharm

import bottle
from bottle import Bottle, template, redirect, request, static_file, response
import app02
root = Bottle()
bottle.TEMPLATE_PATH.append("./tpl/")
import time

# @root.route("/static/<path:path>")
@root.route("/static/path:path")
def static(path):
    print(path) # /static/# path
    return static_file(path, root="static")

@root.route("/index/")
def index():
    if not request.get_cookie("key"):
        response.set_cookie("key", str(time.asctime()))
    return template("index.html", name="Bottle Web")

@root.route("/login/", method=["GET", "POST"])
def login():
    print(request.forms.get("name"))
    print(request.query.get("name"))
    print(request.body)
    print(request.params.get("name"))
    if request.method == "GET":
        return template("login2.html")
    else:

        return request.params.get("name")

root.mount("app02", app02.app02)

root.run(host="127.0.0.1", port=8003, server="tornado")
