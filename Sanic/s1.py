# -*- coding: utf-8 -*-
# @Time    : 18-1-5 下午3:34
# @Author  : Gavin Gan
# @File    : s1.py
# https://github.com/channelcat/sanic

# from sanic import Sanic
# from sanic.response import json
#
# app = Sanic()
#
# @app.route("/")
# async def test(request):
#     return json({"hello": "world"})
#
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8003)

from flask import Flask
app = Flask(__name__)

@app.route("/")
def test():
    return "hello world"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8003)