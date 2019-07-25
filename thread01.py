"""
线程基础使用
"""
from threading import Thread
import time
import os


# 线程函数
def music():
    for i in range(3):
        time.sleep(2)
        print("播放：起风了", os.getpid())


# 创建线程
t = Thread(target=music)
# 启动线程
t.start()
for i in range(4):
    time.sleep(1)
    print("播放：体面", os.getppid())

# 回收线程
t.join()
