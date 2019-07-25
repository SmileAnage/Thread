"""
线程函数传参
"""
from threading import Thread
import time


# 含有参数的线程函数
def fun01(sec_, name):
    time.sleep(sec_)
    print("'%s' 执行完毕" % name)


# 创建多个线程
jobs = []
for i in range(5):
    t = Thread(target=fun01, args=(2,), kwargs={'name': '小木'})
    jobs.append(t)
    t.start()

# 循环回收线程
for i in jobs:
    i.join()
