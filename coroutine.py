# 协程 - 生产者消费者模型
# import time
#
#
# # 消费者
# def consumer(name):
#     print('开始吃包子')
#     while True:
#         new_baozi = yield
#         print('{}吃包子{}'.format(name, new_baozi))
#
#
# # 生产者
# def producer():
#     c1.__next__()
#     c2.__next__()
#
#     n = 0
#     while True:
#         time.sleep(1)
#         print('生产包子{},包子{}'.format(n, n+1))
#         c1.send(n)
#         c2.send(n+1)
#
#         n += 2
#
#
# if __name__ == '__main__':
#     c1 = consumer('c1')
#     c2 = consumer('c2')
#     producer()


############################################
# greenlet: 协程模块
# from greenlet import greenlet
#
#
# def test1():
#     print('2222222')
#     gr2.switch()
#     print('4444444')
#
#
# def test2():
#     print('1111111')
#     gr1.switch()
#     print('3333333')
#     gr1.switch()
#
#
# gr1 = greenlet(test1)
# gr2 = greenlet(test2)
#
# gr2.switch()


###############################################
# gevent模块协程爬取
# import gevent
# import requests, time
#
# start = time.time()
#
#
# def get_html(url):
#     res = requests.get(url)
#     data = res.text
#     print(data, url)
#
#
# gevent.joinall([
#     gevent.spawn(get_html, 'https://www.baidu.com/'),
#     gevent.spawn(get_html, 'https://www.python.org/'),
#     gevent.spawn(get_html, 'https://www.yahoo.com/'),
#     gevent.spawn(get_html, 'https://www.sina.com/'),
#     gevent.spawn(get_html, 'http://www.xiaohuar.com/hua/'),
# ])

#
# get_html('https://www.baidu.com/')
# get_html('https://www.python.org/')
# get_html('https://www.yahoo.com/')
# get_html('https://www.sina.com/')
# get_html('http://www.xiaohuar.com/hua/')


# print(time.time()-start)


l = [
    'a: 1',
    'b: 2',
    'c: 3',
    'd: 4',
]

d = {}

for i in l:
    i = i.split(':')
    key = i[0].strip()
    value = i[1].strip()
    d[key] = value

print(d)
print(type(d))

