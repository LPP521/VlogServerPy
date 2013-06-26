#!/usr/bin/env python
#_*_coding:utf-8_*_

#客户端请求的处理模块

import socket
import MySQLdb
import MySQLdb.cursors

conn = MySQLdb.connect(host='localhost',user='root',passwd='',db='vlog_v1',cursorclass=MySQLdb.cursors.DictCursor)
cur = conn.cursor()
#请求好友列表
def friends(tcpconn):
	'根用户id查询好友列表'
	userid = tcpconn.recv(16)
	cur.execute('select userfriend,friends_name from vl_friend where user = %s',userid)
	res = cur.fetchall()
	print res

#插入视频日志记录
def insertVideoRecord(c):
	buf = c.recv(1024)
	print buf
	title,filename,author,explain =buf.split(',')  # c.recv(1024).split(',')
	print explain
	picture = filename[:-3] + 'jpg' #图片名称和视频名称就后缀名不一样
	videourl = '/var/videohome/'+filename
	cur.execute('insert into vl_video(video_name,video_picture,video_url,video_author,video_date,video_explain) \
				VALUES(%s,%s,%s,%s,NOW(),%s)',(title,picture,videourl,author,explain))
	conn.commit()

def recvFile(c):
	fileType,filename = c.recv(24).split(',')
	#根据文件类型觉定文件的保存路径
	path = ''
	if fileType =='video':
		path = r'/var/videohome/'+filename
	else:
		path = r'/var/imagehome/'+filename
	#开始接收文件
	f = open(path,'wb')
	while True:
		buf = c.recv(1024)
		f.write(buf)
		if not len(buf):
			break
	f.close()


def signin(connect):pass
def offine(conn):pass
def video(c):pass
def videoinfo(c):pass
def mailinfo(c):pass
def close(c):pass

