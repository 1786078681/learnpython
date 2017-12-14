#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-14 下午1:45
# @Author  : Gavin Gan
# @Site    : 
# @File    : flask_server.py
# @Software: PyCharm
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


def wupeiqi():
    return '<h1>Wupeiqi</h1>'


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', ww=wupeiqi, name="Flask name",
                           k1=['a', 'b'], k2=(1,'a'), k3={"name": "tome", "age": 28}

                           )
#
@app.route('/test/<any(about, help, imprint, class, "foo,bar"):page_name>')
def test(page_name):
    return page_name

@app.route("/index/", methods=["GET", "POST"])
def hello():
    print(request.args)

    # return "hello"
    # return redirect('/test/about')
    url = url_for('test', page_name="about") # /test/
    return redirect(url)

if __name__ == "__main__":
    app.run(port=8004)