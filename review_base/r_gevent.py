# -*- coding: utf-8 -*-
# @Time    : 18-1-11 下午1:32
# @Author  : Gavin Gan
# @File    : r_gevent.py
import gevent
from gevent import monkey, socket
monkey.patch_socket()
import requests
import time
urls = ['www.google.com.hk', 'www.example.com', 'www.python.org']

def f1(url):
    response = requests.get(url)
    print('sleep no do ')
    time.sleep(5)

    print(response.headers)


jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]

gevent.joinall(jobs, timeout=2)

print([job.value for job in jobs])

