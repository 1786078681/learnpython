# -*- coding: utf-8 -*-
# @Time    : 18-1-8 上午9:58
# @Author  : Gavin Gan
# @File    : tw_server.py
# coding=utf-8
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory

class SimpleProtocol(Protocol):
    def connectionMade(self):
        """客户端连入后向客户端发送一条消息Hello"""
        print 'success from ', self.transport.client
        self.transport.write("Hello")

    def connectionLost(self, reason):
        print self.transport.client, 'disconnected'
        print reason

    def dataReceived(self, data):
        print data

factory = Factory()
factory.protocol = SimpleProtocol

# 在9001端口进行监听
reactor.listenTCP(9001, factory)
# 启动事件循环
reactor.run()
