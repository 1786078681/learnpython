# -*- coding: utf-8 -*-
# @Time    : 18-1-10 下午2:55
# @Author  : Gavin Gan
# @File    : test.py


import sys, os

list1Display = ['1', '2', '3']
list2Display = ['abc', 'def', 'rfs']
while list2Display != []:
    # Prints the values to a stream, or to sys.stdout by default.
    # Optional keyword arguments:
    # file: a file-like object (stream); defaults to the current sys.stdout.
    # sep:  string inserted between values, default a space.
    # end:  string appended after the last value, default a newline.
    # print 可以将值输出到指定的输出流(可以是文件句柄),若不指定，
    # 则输出到stdout(标准输出)
    # 一般我们使用的时候不加输出定向符“>>”到输出的file对象，本代码中对象是stdout
    # 下面的print在stdout对象中每次输出两个值
    print >> sys.stdout, list2Display.pop(), list1Display.pop()
os.system("pause")