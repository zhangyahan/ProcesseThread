# import threading  # 线程
# import time
#
#
# def Hi(num):
#     print('hello {}'.format(num))
#     time.sleep(3)
#
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=Hi, args=(10,))
#     t1.start()
#     t2 = threading.Thread(target=Hi, args=(9,))
#     t2.start()



# 守护线程
# 在start前设置setDaemon为True
#


# def test1():
#     print('test1', time.ctime())
#     time.sleep(3)
#     print('test1', time.ctime())
#
#
# def test2():
#     print('test2', time.ctime())
#     time.sleep(5)
#     print('test1', time.ctime())
#
#
# lst = []
#
# t1 = threading.Thread(target=test1)
# t2 = threading.Thread(target=test2)
#
# lst.append(t1)
# lst.append(t2)
#
# if __name__ == '__main__':
#     t2.setDaemon(True)
#     for i in lst:
#         i.start()

# 调用方式2: ############################################


# class MyThread(threading.Thread):
#
#     def __init__(self, num):
#         threading.Thread.__init__(self)
#         self.num = num
#
#     # 重写run函数
#     def run(self):
#         print('{} {}'.format(self.num, time.ctime()))
#         print('running on number:{}'.format(self.num))
#         time.sleep(3)
#         print('{} {}'.format(self.num, time.ctime()))
#
#
# if __name__ == '__main__':
#     t1 = MyThread(1)
#     t2 = MyThread(2)
#     t1.start()
#     t2.start()
#     print('ending')

