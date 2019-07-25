"""
线程Event　同步互斥
"""
from threading import Event
from threading import Thread

s = None  # 用于通信
e = Event()  # 事件对象


def fun01():
    print("杨子荣前来拜山头")
    global s
    s = '天王盖地虎'
    e.set()  # 操作完成共享 e 设置


# 创建线程对象
t = Thread(target=fun01)
t.start()

print("说对口令就是自己人")
e.wait()  # 阻塞等待

if s == '天王盖地虎':
    print("宝塔镇河妖")
    print("口令正确")
else:
    print("嫩死他")

t.join()
