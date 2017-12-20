import requests
import concurrent.futures
import time

start = time.time()
def fun1():
    requests.get("http://localhost:9000/users/login?next=/")


with concurrent.futures.ThreadPoolExecutor(max_workers=9999) as executor:
    for i in range(2000):
        executor.submit(fun1)

print(time.time() - start)
