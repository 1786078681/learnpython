#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-8 下午5:27
# @Author  : Gavin Gan
# @Site    : 
# @File    : server1.py
# @Software: PyCharm

from wsgiref.simple_server import make_server

def view_abc(request):

    s = "hello, workd"
    return [b'']

def application(environ, start_response):
    print(environ.get("PATH_INFO"))
    start_response('200 OK', [("content-type", "text/html")])
    if environ.get("PATH_INFO") == "/abc":
        return view_abc(environ)
    else:
        return [b'Hellow, Web']



httpd = make_server('', 8003, application)

print("Server HTTP on port 8003")
httpd.serve_forever()