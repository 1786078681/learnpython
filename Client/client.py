# -*- coding: utf-8 -*-
# @Time    : 18-1-5 下午3:35
# @Author  : Gavin Gan
# @File    : client.py

import threading
import requests

def f1(url, method, i):
    # print("get: ", url)
    response = requests.request(method, url)
    # print(response.content)
    sem.release()

sem = threading.BoundedSemaphore(1000)
p = []
for i in range(2000):
    sem.acquire()
    t = threading.Thread(target=f1, args=("http://127.0.0.1:8003/", "get", i))
    p.append(t)
    t.start()

for t in p:
    t.join()