# -*- coding: utf-8 -*-
# @Time    : 18-1-10 下午5:36
# @Author  : Gavin Gan
# @File    : select_server.py
import socket
import queue
import select
server_address = ('localhost', 10000)
server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

server.setblocking(False)
server.bind(server_address)

server.listen(100)

inputs = [server]
outputs = []
message_queue = {}

while inputs:
    print("wait for next event...")
    readable, writeable, exceptional = select.select(inputs, outputs, inputs)

    for s in readable:
        if s is server:

            connections, addr = s.accept()
            print("Hello! New connection.", addr)
            connections.setblocking(False)
            # message_queue.setdefault(connections, queue.Queue())
            message_queue[connections] = queue.Queue()
            inputs.append(connections)

        else:
            data = s.recv(1024)
            if data:
                message_queue[s].put(data)
                print("recv data %s from %s: " % (data, s.getpeername()))
                if s not in outputs:
                    outputs.append(s)
            else:
                print("client closed")
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()

    for s in writeable:
        try:
            data = message_queue[s].get_nowait()
        except queue.Empty:
            # print("The %s is empty! " % s.getpeername())
            print('output queue for', s.getpeername(), 'is empty')
            outputs.remove(s)
        else:
            print("send data %s to %s: ", (data.upper(), s.getpeername()))
            s.send(data.upper())

    for s in exceptional:
        print("exception ---> ", s.getpeername())
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)

        s.close()

        del message_queue[s]

