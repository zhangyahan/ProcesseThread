# import threading
# import time
#
#
# # 同步锁,保证数据的一致性
# def sub():
#     global num
#     # num -= 1
#     print('OK')
#     # 获取上锁, 上同步锁的代码执行为串行执行
#     lock.acquire()
#     temp = num
#     time.sleep(0.0001)
#     num = temp - 1
#     # 释放锁
#     lock.release()
#
#
# num = 100
#
# lst = []
# # 创建锁对象
# lock = threading.Lock()
#
# for i in range(100):
#     t = threading.Thread(target=sub)
#     lst.append(t)
#     t.start()
#
# for i in lst:
#     i.join()
#
# print(num)


###########################################################
# 线程死锁和递归锁(可重入锁)
# import threading
# import time
#
#
# class MyThread(threading.Thread):
#
#     def action_A(self):
#         r_lock.acquire()
#         print(self.name, 'gotA', time.ctime())
#         time.sleep(2)
#
#         r_lock.acquire()
#         print(self.name, 'gotB', time.ctime())
#         time.sleep(1)
#
#         r_lock.release()
#         r_lock.release()
#
#     def action_B(self):
#         r_lock.acquire()
#         print(self.name, 'gotB', time.ctime())
#         time.sleep(2)
#
#         r_lock.acquire()
#         print(self.name, 'gotA', time.ctime())
#         time.sleep(1)
#
#         r_lock.release()
#         r_lock.release()
#
#     def run(self):
#         self.action_A()
#         self.action_B()
#
#
# if __name__ == '__main__':
#     # 同步锁
#     # A = threading.Lock()
#     # B = threading.Lock()
#
#     # 递归锁
#     r_lock = threading.RLock()
#
#     lst = []
#     for i in range(5):
#         t = MyThread()
#         lst.append(t)
#         t.start()
#     for i in lst:
#         i.join()
#     print('ending....')


################################################
# 同步对象(event事件)
# import threading
# import time
#
#
# class Boss(threading.Thread):
#     def run(self):
#         print('Boss: 今晚大家都要加班到22:00')
#         print(event.isSet())
#         event.set()  # 设置event状态
#         time.sleep(5)
#         print('Boss: <22:00>可以下班了')
#         print(event.isSet())
#         event.set()  # 设置event状态
#
#
# class Worker(threading.Thread):
#     def __init__(self, pope):
#         threading.Thread.__init__(self)
#         self.pope = pope
#
#     def run(self):
#         event.wait()  # 一旦event被设定,等同于pass
#         print('Worker{}: 哎.....命苦啊'.format(self.pope))
#         time.sleep(1)
#         event.clear()  # event状态清空
#         event.wait()  # 等待
#         print('Worker{}: OhYeah'.format(self.pope))
#
#
# if __name__ == '__main__':
#     # event对象是线程共有的,判断event状态,isSet(),返回bool
#     # 如果没有被set(),则wait()一直阻塞
#     # clear()清除状态
#     event = threading.Event()
#
#     threads = []
#     for i in range(5):
#         threads.append(Worker(i))
#     threads.append(Boss())
#
#     for t in threads:
#         t.start()
#
#     for t in threads:
#         t.join()
#
#     print('end......')


###################################################
# 信号量
# import threading
# import time
#
#
# class MyThread(threading.Thread):
#
#     def run(self):
#         # 判断锁状态,返回bool
#         if semaphore.acquire():
#             print(semaphore.acquire())
#             print(self.name)
#             time.sleep(3)
#             # 解锁
#             semaphore.release()
#
#
# if __name__ == '__main__':
#     # 设置信号量为5,
#     semaphore = threading.Semaphore(5)
#
#     threads = []
#
#     for i in range(100):
#         t = MyThread()
#         threads.append(t)
#         t.start()
#
#     for t in threads:
#         t.join()
#
#     print('ending......')

#################条件####################
# from threading import Condition, Thread


# def condition():
#     ret = False
#     inp = input('>>>')
#     if inp == 'True':
#         ret = True
#     else:
#         ret = False
#     return ret


# def run(i, con):
#     print(i)
#     con.acquire()  # 对条件进行上锁
#     con.wait_for(condition)  # 等待条件成立
#     print(i + 100)
#     con.release()  # 解除条件


# if __name__ == "__main__":
#     con = Condition()  # 创建条件对象
#     for i in range(10):
#         t = Thread(target=run, args=(i, con))
#         t.start()
    # while 1:
    #     inp = input('>>>')
    #     if inp == 'Q':
    #         break
    #     con.acquire()
    #     con.notify(int(inp))
    #     con.release()


##############定时器################
# from threading import Timer

# def hello():
#     print('hello')

# t = Timer(3, hello)
# t.start()


##########################################
# 消息队列
# 存放数据的三种模式
# FIFO(默认先进先出)
# import queue  # 线程队列
# import threading


# ques = queue.Queue(maxsize=3)  # 创建线程消息队列对象,可以指定大小
# ques = queue.LifoQueue()  # 后进先出
# ques = queue.PriorityQueue()  # 优先级put([优先级 1> , 数据]) get()返回列表
# ques.put(1)  # 放数据
# ques.put(2)  # 放数据
# ques.put(3, block=False)  # 放数据,设置block为False队列满时提示异常
# ques.put(3)  # 放数据,当消息队列满时阻塞
#
# while 1:
#     que1 = ques.get()  # 取数据,当消息队列空则阻塞
#     que2 = ques.get(block=False)  # 取数据,设置False队列空提示异常
#     print(que1)
#     print(que2)
#     print('-------------')
#     print(q.qsize())  # 已存在消息的队列大小
#     print(q.empty())  # 是否为空
#     print(q.full())  # 是否为满
#     print(q.task_done())  # 当操作完后,发送一个信号
#     print(q.join())  # 等待队列为空,在执行其他操作


############################################
# 生产者消费者模型
# import time
# import random
# import queue
# import threading


# q = queue.Queue()


# def producer(name):
#     count = 0
#     while count < 10:
#         print('making.....')
#         time.sleep(5)
#         q.put(count)
#         print('{}生产了包子{}'.format(name, count))
#         count += 1
        # q.task_done()  # 发送做好了包子的信号
        # q.task_done() 和 q.join() 必须成对出现,在不同的线程中
        # q.join()  # 等待用户吃完包子
        # print('OK...')


# def consumer(name):
#     count = 0
#     while count < 10:
#         time.sleep(random.randrange(4))
        # if not q.empty():  # 判断是否为空
        # print('waiting......')
        # data = q.get()
        # print('eating....')
        # time.sleep(4)
        # q.task_done()  # 发送吃完包子的信号
        # q.join()  # 收到了包子做好的信号,执行以下代码
        # print('{}吃了包子{}'.format(name, data))
        # else:
        #     print('没有包子啦')
        # count += 1


# if __name__ == '__main__':
    # t1 = threading.Thread(target=producer, args=('A君',))
    # t2 = threading.Thread(target=consumer, args=('B君',))
    # t3 = threading.Thread(target=consumer, args=('C君',))
    # t4 = threading.Thread(target=consumer, args=('D君',))

    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()

    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
