#!/usr/bin/env python
#_*_coding:utf-8_*_
import socket
from SocketServer import TCPServer,ThreadingMixIn,BaseRequestHandler
import request_handler as handler

requestCommandAction = {
	'signin':handler.signin,	#用户登录
	'friends':handler.friends,	#请求好友信息
	'offine':handler.offine,	#下线
	'video':handler.video,		#请求视频文件
	'videoinfo':handler.videoinfo,	#请求视频附加信息
	'mailinfo':handler.mailinfo,	#请求视频邮件的信息
	'close':handler.close,		#本次请求结束，关闭连接
	'videodb':handler.insertVideoRecord,#插入一条视频日志记录
	'sendmail':handler.insertMailRecord,#插入一条视频邮件记录
	'UP':handler.recvFile				#接收来自客户端的一个文件传输
}
HOST = '121.199.24.119'
PORT = 8000 

class VlogServer(ThreadingMixIn,TCPServer): pass

class VlogHandler(BaseRequestHandler):
	def handle(self):
		data = self.request.recv(8)
		if data in requestCommandAction:
			self.request.send('yes')
			requestCommandAction[data](self.request)
		else:
			self.request.send('no')
		self.request.close()

vlogServer = VlogServer((HOST,PORT),VlogHandler)
vlogServer.serve_forever()

