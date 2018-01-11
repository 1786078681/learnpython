# -*- coding: utf-8 -*-
# @Time    : 18-1-11 下午1:12
# @Author  : Gavin Gan
# @File    : server_socket.py
import socket



s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
listen_address = ('localhost', 10000)
s.setblocking(False)
s.bind(listen_address)

s.listen(5)
connections = []
while True:
    conn, addr = s.accept()
    connections.append(conn)

    print("The New connect, ", addr)
    while True:
        print("connections count: ", len(connections))
        data = conn.recv(1024)
        if data:
            print("recv data: ", data)

            conn.send(data.upper())
        else:
            print(addr, "was lost")
            break
    connections.remove(conn)