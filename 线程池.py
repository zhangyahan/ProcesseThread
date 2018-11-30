# 一个容器
# 取一个少一个
# 无线程时等待
# 线程执行完毕,交还线程

# 低级版线程池
# import queue
# import threading
# import time

# class ThreadPool:
#     def __init__(self, maxsize=5):
#         # 初始化函数
#         self.maxszie = maxsize  # 定义最大容量
#         self._q = queue.Queue(maxsize)  # 创建管道对象
#         for i in range(maxsize):
#             self._q.put(threading.Thread)  # 将线程对象放入管道中

#     def get_thread(self):
#         return self._q.get()  # 获取管道对象

#     def add_thread(self):
#         self._q.put(threading.Thread)  # 添加管道对象


# pool = ThreadPool(5)  # 创建实例


# def tast(arg, p):
#     print(arg)
#     time.sleep(1)
#     p.add_thread()  # 添加线程对象


# for i in range(100):
#     # 获取threading.Thread类
#     t = pool.get_thread()
#     obj = t(target=tast, args=(i,pool,))
#     obj.start()



# 牛逼的线程池
# import queue
# import threading
# import contextlib

# StopeEvent = object()

# class ThreadPool(object):
#     def __init__(self, max_num, max_task_num=None):
#         if max_task_num:
#             self.q = queue.Queue(max_task_num)
#         else:
#             self.q = queue.Queue()
#         self.max_num = max_num
#         self.cancel = False
#         self.termimal = False
#         self.generate_list = []
#         self.free_list = []
    
#     def run(self, func, *args, callback=None):

#################线程池and进程池#####################
import time
from concurrent.futures import ThreadPoolExecutor  # 线程池
from concurrent.futures import ProcessPoolExecutor  # 进程池


def func(n):
    time.sleep(2)
    print(n)
    return n * n

# tpool = ThreadPoolExecutor(max_workers=5)  # 创建线程池, 不要超过cpu个数*5
tpool = ProcessPoolExecutor(max_workers=5)  # 创建线程池, 不要超过cpu个数*5
t_list = []
for i in range(20):
    t = tpool.submit(func, i)  # 异步提交
    t_list.append(t)

tpool.shutdown()  # close+join:阻塞等待线程池中的任务执行完毕
print('主线程')
for t in t_list:print('********', t.result())


        



 





