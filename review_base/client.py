# -*- coding: utf-8 -*-
# @Time    : 18-1-11 下午1:16
# @Author  : Gavin Gan
# @File    : client.py.py
import socket
import threading


messages = [b'hello', b'I is gold', b'bye']

clients = [socket.socket() for x in range(100)]
listen_address = ('localhost', 10000)
import time
def f1(c):
    c.connect(listen_address)

    for msg in messages:
        c.send(msg)
        time.sleep(5)
        print(c.recv(1024))
    c.close()

p = []

for c in clients:
    t = threading.Thread(target=f1, args=(c,))
    t.start()
    p.append(t)
for t in p:
    t.join()

print("end...")

