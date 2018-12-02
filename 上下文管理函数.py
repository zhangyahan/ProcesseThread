#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-02 18:56:08
# @Author  : Zhang Yahan (zyahan1997@163.com)
# @Link    : http://www.github.com/zhangyahan/
# @Version : $Id$

import contextlib
import socket

# @contextlib.contextmanager
# def test1():
# 	print('我是test1中yield前的文字')
# 	yield
# 	print('我是test1中yield后的文字')


# with test1():
# 	print('我是test2中的文字')


# 使用contextlib.contextmanager进行上下文管理
@contextlib.contextmanager
def create_socket(ip, port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind((ip, port))
	sock.listen(5)
	try:
		yield sock
	except Exception as e:
		raise e
	finally:
		sock.close()

with create_socket('127.0.0.1', 9999) as sock:
	print(sock)
