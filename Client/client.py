# -*- coding: utf-8 -*-
# @Time    : 18-1-5 下午3:35
# @Author  : Gavin Gan
# @File    : client.py

import threading
import requests, socket
import concurrent.futures

def f1(url, method, i):
    # print("get: ", url)
    response = requests.request(method, url,timeout=1)
#    print(response.content)
    # s = socket.socket()
    # s.connect(("127.0.0.1", 9001))
    # recv = s.recv(1024)
    # # print(recv)
    # s.close()
    # sem.release()

# sem = threading.BoundedSemaphore(2500)
# p = []
# for i in range(500):
#     sem.acquire()
#     t = threading.Thread(target=f1, args=("http://127.0.0.1:8003/", "get", i))
#     p.append(t)
#     t.start()
#
# for t in p:
#     t.join()

url = {'': 3, '/test/': 5, '/admin/': 1}
weight = 9
s = {}
# '':[0:3], [3:5], [5:1]
with concurrent.futures.ThreadPoolExecutor(max_workers=1500) as e:
    for i in range(1,2000, 9):
        for k,v in url.items():
            # 3, [i+0:3], 0,1,2  ## 5, [i+9:5+3], ### 1,[i+9:1+5+3]
            #
            #
            for j in range(v):
                e.submit(f1, "http://127.0.0.1:8003" + k, "get", i)
                if k not in s:
                    s.setdefault(k, 1)
                else:
                    s[k] += 1
                # print("http://127.0.0.1:8003" + k)

print(s)
