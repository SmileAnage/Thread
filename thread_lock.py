"""
线程锁
"""
from threading import Lock
from threading import Thread

a = b = 0
lock = Lock()  # 定义锁


def value():
    while True:
        lock.acquire()  # 上锁
        if a != b:
            print("a = %d, b = %d" % (a, b))
        lock.release()  # 解锁


t = Thread(target=value)
t.start()
while True:
    # 自动上锁，结束自动解锁
    with lock:  # 上锁
        a += 1
        b += 1
        # 自动解锁

t.join()

