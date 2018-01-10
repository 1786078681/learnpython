# -*- coding: utf-8 -*-
# @Time    : 18-1-9 下午2:08
# @Author  : Gavin Gan
# @File    : flask_ao.py


from  flask import Flask, request
import time,json
app = Flask(__name__)

@app.route("/")
def hello():
    print(request.headers.get("User-Agent"))
    time.sleep(3)
    print("end block")
    return json.dumps({"hello": "abc"})

app.run(port=8003)