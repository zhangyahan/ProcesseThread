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
import queue
import threading
import contextlib
import time

StopeEvent = object()

class ThreadPool(object):

    def __init__(self, max_num, max_task_num=None):
        if max_task_num:
            self.q = queue.Queue(max_task_num)
        else:
            self.q = queue.Queue()
        self.max_num = max_num
        self.cancel = False
        self.termimal = False
        self.generate_list = []
        self.free_list = []
    
    def run(self, func, args, callback=None):
    	"""
		线程池执行一个任务
		:param func: 任务函数
		:param args: 任务函数所需参数
		:param callback: 任务执行失败或成功后执行的回调函数
						 会掉函数有两个参数,
						 1,任务函数执行状态
						 2,任务函数返回值(默认为None,即不执行毁掉函数)
		:return: 如果线程池已经终止,则返回True否则None
    	"""
    	if self.cancel:  # 初始为False
    		return
    	if len(self.free_list) == 0 and len(self.generate_list) < self.max_num:
    		# self.free_list初始为0   self.generate_list初始为0  self.max_num为用户传递进来的线程数
    		self.generate_thread()

    	w = (func, args, callback,)
    	self.q.put(w)

    def generate_thread(self):
    	"""
		创建一个线程, 执行self.call方法
    	"""
    	t = threading.Thread(target=self.call)
    	t.start()

    def call(self):
    	"""
		循环去获取任务函数并执行任务函数
    	"""
    	current_thread = threading.current_thread()  # 获取现在的线程
    	self.generate_list.append(current_thread)  # 将线程添加到generate_list中

    	event = self.q.get()
    	print(event)
    	while event != StopeEvent:
    		func, arguments, callback = event
    		try:
    			result = func(*arguments)
    			success = True
    		except Exception as e:
    			result = None
    			success = False

    		if callback is not None:
    			try:
    				callback(success, result)
    			except Exception as e:
    				pass

    		with self.worker_state(self.free_list, current_thread):
    			if self.termimal:
    				event = StopeEvent
    			else:
    				event = self.q.get()

    	else:
    		self.generate_list.remove(current_thread)

    def close(self):
    	"""
		执行完所有任务后,所有线程停止
    	"""
    	self.cancel = True
    	full_size = len(self.generate_list)
    	while full_size:
    		self.q.put(StopeEvent)
    		full_size -= 1

    def terminate(self):
    	"""
		无论是否还有任务,终止线程
    	"""
    	self.termimal = True

    	while self.generate_list:
    		self.q.put(StopeEvent)

    	self.q.queue.clear()

    @contextlib.contextmanager
    def worker_state(self, state_list, worker_thread):
    	"""
    	用于记录线程中正在等待的线程数
    	"""
    	state_list.append(worker_thread)
    	try:
    		yield
    	except Exception as e:
    		pass
    	finally:
    		state_list.remove(worker_thread)


# 调用
pool = ThreadPool(5)

def callback(status, result):
	pass


def action(i):
	print(i)


for i in range(30):
	ret = pool.run(action, i, callback)

time.sleep(5)
print(len(pool.generate_list), len(pool.free_list))
print(len(pool.generate_list), len(pool.free_list))
pool.close()
pool.terminate()



#################线程池and进程池#####################
# import time
# from concurrent.futures import ThreadPoolExecutor  # 线程池
# from concurrent.futures import ProcessPoolExecutor  # 进程池


# def func(n):
#     time.sleep(2)
#     print(n)
#     return n * n

# # tpool = ThreadPoolExecutor(max_workers=5)  # 创建线程池, 不要超过cpu个数*5
# tpool = ProcessPoolExecutor(max_workers=5)  # 创建线程池, 不要超过cpu个数*5
# t_list = []
# for i in range(20):
#     t = tpool.submit(func, i)  # 异步提交
#     t_list.append(t)

# tpool.shutdown()  # close+join:阻塞等待线程池中的任务执行完毕
# print('主线程')
# for t in t_list:print('********', t.result())


        



 





