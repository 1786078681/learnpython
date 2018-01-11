# -*- coding: utf-8 -*-
# @Time    : 18-1-11 下午1:55
# @Author  : Gavin Gan
# @File    : r_redis.py
import redis

# conn = redis.Redis(host="localhost", port=6379, db=5)
# conn.set('foo', 'py redis')
# print(conn.get('foo'))



pool = redis.ConnectionPool(host='localhost', port=6379, db=5)

conn = redis.Redis(connection_pool=pool)

print(conn.get('foo'))
print(conn.get('name').decode('utf-8'))
conn.bitcount('online')

'''
set(name, value, ex=None, px=None, nx=False, xx=False)
setnx(name, value)
setex(name, value, time)
psetex k time_ms v
mset k1 v1 k2 v2
get
mget k1 k2 
getset
getrange
### hash
hset k k1 v1
hmset k k2 v2 k3 v3
hget k k2
hmget k k2 k3
hgetall k
helen k
hkyes k
hvals k
hexists k k2
 ### list
127.0.0.1:6379[5]> linsert o2 before a 'A'
(integer) 7
127.0.0.1:6379[5]> LRANGE o2 0 10
1) "b"
2) "A"
3) "a"
4) "7"
5) "8"
6) "9"
7) "10"
127.0.0.1:6379[5]> linsert o2 after a 'B'
(integer) 8
127.0.0.1:6379[5]> LRANGE o2 0 10
1) "b"
2) "A"
3) "a"
4) "B"
5) "7"
6) "8"
7) "9"
8) "10"

'''