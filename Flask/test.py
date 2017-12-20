#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-12-18 下午3:34
# @Author  : Gavin Gan
# @Site    : 
# @File    : test.py
# @Software: PyCharm
from werkzeug.wrappers import Response, Request
from werkzeug.serving import run_simple

@Request.application
def hello(request):
    return Response("hello World.")

if __name__ == '__main__':
    run_simple("localhost", 8001, hello)