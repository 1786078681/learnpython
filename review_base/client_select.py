# -*- coding: utf-8 -*-
# @Time    : 18-1-10 下午5:15
# @Author  : Gavin Gan
# @File    : client_select.py.py

import socket, time
import concurrent.futures

socks = [socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) for x in range(1000)]

messages = [b"1 hello", b"Go!", b"Bye"]
server_address = ('localhost', 10000)

for s in socks:
    print(s)
    s.connect(server_address)

print("start....")
# for m in messages:
#
#     for s in socks:
#         print("name: %s, msg: %s" % (s.getsockname(), m))
#         s.send(m)
#
#     for s in socks:
#         data = s.recv(1024)
#         print('%s: received "%s"' % (s.getsockname(), data.decode()))
#         if not data:
#             print('closing socket, ', s.getsockname())
#             s.close()

def f(s, m):

    print("name: %s, msg: %s" % (s.getsockname(), m))
    s.send(m)
    data = s.recv(1024)
    print('%s: received "%s"' % (s.getsockname(), data.decode()))
    if not data:
        print("closing socket", s.getsockname())
        s.close()

with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as e:
    for m in messages:
        for s in socks:
            e.submit(f, s, m)





