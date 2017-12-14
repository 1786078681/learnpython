#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-14 上午10:29
# @Author  : Gavin Gan
# @Site    : 
# @File    : app02.py
# @Software: PyCharm


from bottle import template, Bottle

app02 = Bottle()

@app02.route('/hello/', method='GET')
def index():
    # return template('<b>App02</b>!')
    return 'App02'

@app02.get("/")
def home():
    return 1