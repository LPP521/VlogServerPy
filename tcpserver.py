#!/usr/bin/env python
#_*_coding:utf-8_*_
import socket
import request_handler as handler
#address
PORT = 8000


#configure socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",PORT))

#passively wait
s.listen(5)
#accept and establish connection
while True:
	c,addr = s.accept()
	print 'Got connection from',addr
	request = ''
	while True:
		request = c.recv(16)
		if request == 'signin':
			#登录,TO DO
			continue
		elif request == 'friends':
			#请求好友列表，doing
			handler.friends(c)			
		elif request == 'offine':
			#下线，TO DO
			continue
		elif request == 'log':
			#请求日志
			continue
		elif request == 'mail':
			#请求邮件
			continue
		elif request == 'over':
			#请求结束
			break
		else:
			#不能识别请求信息
			c.send('invalid')
			break
	

