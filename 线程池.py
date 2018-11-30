# 一个容器
# 取一个少一个
# 无线程时等待
# 线程执行完毕,交还线程

# 低级版线程池
# import queue
# import threading
# import time
# 
# class ThreadPool:
#     def __init__(self, maxsize=5):
#         self.maxszie = maxsize
#         self._q = queue.Queue(maxsize)
#         for i in range(maxsize):
#             self._q.put(threading.Thread)
# 
#     def get_thread(self):
#         return self._q.get()
# 
#     def add_thread(self):
#         self._q.put(threading.Thread)
# 
# 
# pool = ThreadPool(5)
# 
# 
# def tast(arg, p):
#     print(arg)
#     time.sleep(1)
#     p.add_thread()
# 
# 
# for i in range(100):
#     # 获取threading.Thread类
#     t = pool.get_thread()
#     obj = t(target=tast, args=(i,pool,))
#     obj.start()



# 牛逼的线程池





# from threading import Timer
# 
# 
# def hello():
#     print('hello world')
# 
# t = Timer(1, hello)
# t.start() 





