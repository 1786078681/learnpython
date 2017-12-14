#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-14 下午4:55
# @Author  : Gavin Gan
# @Site    : 
# @File    : s1.py
# @Software: PyCharm
from flask import Flask, session, redirect, render_template, flash, get_flashed_messages, request, make_response

app = Flask(__name__)

@app.route("/index/")
def index():
    if not session.get("name"):
        session.setdefault("name", "session name")

    resp = make_response(render_template("index.html", name="Session Test"))
    if not request.cookies.get("index_cookie"):
        resp.set_cookie("index_cookie", "cookie index_cookie", path="/index/")
    print(request.cookies.get("name1"))
    return resp

@app.route("/")
def home():
    return "OK"

app.secret_key = 'f3dv&89)_Z./,?~a*21@#2'

if __name__ == "__main__":

    app.run(port=8003)