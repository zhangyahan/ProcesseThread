###########################################
# 调用方法-1
# import time
# from multiprocessing import Process
#
#
# def func(name):
#     time.sleep(1)
#     print('hello:'.format(name), time.ctime())
#
#
# if __name__ == '__main__':
#     p_list = []
#     for i in range(3):
#         p = Process(target=func, args=('whh',))
#         p_list.append(p)
#         p.start()
#
#     for i in p_list:
#         i.join()
#     print('ending...')


#####################################################
# 调用方法-2
# import time
# from multiprocessing import Process
#
#
# class MyProcess(Process):
#     def run(self):
#         time.sleep(1)
#         print('hello:{}'.format(self.name), time.ctime())
#
#
# if __name__ == '__main__':
#     p_list = []
#     for i in range(3):
#         p = MyProcess()
#         p.daemon = True  # 守护进程,主进程运行完后不管子进程,直接结束
#         p_list.append(p)
#         p.start()
#
#     # for p in p_list:
#     #     p.join()
#
#     print('ending...')


####################################
#
# import time
# from multiprocessing import Process
#
#
# class MyProcess(Process):
#     def __init__(self, num):
#         Process.__init__(self)
#         self.num = num
#
#     def run(self):
#         time.sleep(1)
#         print(self.is_alive(), self.num, self.pid)
#
#
#
#
# if __name__ == '__main__':
#     p_list = []
#     for i in range(10):
#         p = MyProcess(i)
#         p_list.append(p)
#
#     for i in p_list:
#         i.start()
#
#     for i in p_list:
#         i.join()
#     print('ending...')


########################################
# 进程间通信 - 进程队列 Queue
# from multiprocessing import Queue  # 进程队列
# import multiprocessing
#
#
# def foo1(q):
#     print(id(q))
#     q.put(123)
#     q.put('hello world')
#
#
# def foo2(q):
#     print(id(q))
#     print(q.get())
#     print(q.get())
#
#
# if __name__ == '__main__':
#     q = Queue()  # 创建进程管道
#     print(id(q))
#     p1 = multiprocessing.Process(target=foo1, args=(q,))
#     p2 = multiprocessing.Process(target=foo2, args=(q,))
#
#     p1.start()
#     p2.start()
#
#     p1.join()
#     p2.join()


##########################################
# 管道通信 - Pipe
# import multiprocessing
#
#
# def f(conn):
#     conn.send([12, {"name": 'Yuan'}, 'hello'])  # 向管道发送数据
#     response = conn.recv()  # 阻塞接受数据
#     print(response)
#     conn.close()  # 关闭管道
#     print('q_ID2', id(conn))
#
#
# if __name__ == '__main__':
#     parent_conn, child_conn = multiprocessing.Pipe()  # 双向管道
#     print('q_ID1', id(child_conn))
#     p = multiprocessing.Process(target=f, args=(child_conn,))
#     p.start()
#     print(parent_conn.recv())  # 阻塞接受数据
#     parent_conn.send('儿子你好!')  # 发送数据


###############################################
# 进程数据共享 - Managers
# import multiprocessing
#
#
# def foo(dic, lst, num):
#     dic['name'] = 'whh'
#     dic['age'] = 12
#     dic['num'] = num
#     lst.append(num)
#
#
# if __name__ == '__main__':
#     manages = multiprocessing.Manager()  # 创建对象
#     dic = manages.dict()  # 定义字典
#     lst = manages.list(range(5))  # 定义列表
#     print(dic, lst)
#
#     p_list = []
#     for i in range(10):
#         p = multiprocessing.Process(target=foo, args=(dic, lst, i))
#         p_list.append(p)
#         p.start()
#
#     for i in p_list:
#         i.join()
#     print(dic, lst)
#     print('main ending.......')


##############################################
# 进程同步
# from multiprocessing import Process, Lock
#
#
# def f(lock, num):
#     with lock:  # 上锁
#         # lock.acquire()
#         print('hello world', num)
#         # lock.release()
#
#
# if __name__ == '__main__':
#     lock = Lock()  # 创建同步锁对象
#
#     for num in range(10):
#         p = Process(target=f, args=(lock, num))
#         p.start()


###############################################
# 进程池
import os
import time
from multiprocessing import Process, Pool


# 子进程函数
def Foo(i):
    time.sleep(1)
    print(i)
    print('Foo pid', os.getpid())
    # return回去的值有回调函数接收
    return 'HELLO {}'.format(i)


# 回调函数被调用时在主进程下执行
def Bar(arg):
    print('Bar', arg)


if __name__ == '__main__':
    pool = Pool(5)  # 创建进程池对象
    print('main pid', os.getpid())
    for i in range(100):
        # pool.apply(func=Foo, args=(i,))  # 同步接口
        # pool.apply_async(func=Foo, args=(i,))  # 异步接口
        # 回调函数: 某个动作或者函数执行成功后再去执行的函数
        pool.apply_async(func=Foo, args=(i,), callback=Bar)

    pool.close()
    pool.join()  # join与close调用顺序是固定的

    print('ending....')
