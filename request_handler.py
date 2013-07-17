#!/usr/bin/env python
#_*_coding:utf-8_*_

#客户端请求的处理模块

import socket
import MySQLdb
import MySQLdb.cursors
import struct

conn = MySQLdb.connect(host='localhost',user='',passwd='',db='vlog_v1',charset='utf8',cursorclass=MySQLdb.cursors.DictCursor)
cur = conn.cursor()
#请求好友列表
def friends(tcpconn):
	'根用户email查询好友列表'
	user_email = tcpconn.recv(50)
	cur.execute('select userfriend,friends_name from vl_friend where user = %s',user_email)
	buf = u''
	for item in cur.fetchall():
		buf = buf + item['userfriend'] + ',' + item['friends_name'] + ','
	buf = buf[:-1]
	buf = buf.encode('utf8')
	buf = struct.pack('B',len(buf))+buf
	tcpconn.send(buf)


#插入视频日志记录
def insertVideoRecord(c):
	buf = c.recv(1024)
#	print buf
	title,filename,author,explain =buf.split(',')  # c.recv(1024).split(',')
	picture = filename[:-3] + 'jpg' #图片名称和视频名称就后缀名不一样
	videourl = 'video/'+filename
	cur.execute('insert into vl_video(video_name,video_picture,video_url,video_author,video_date,video_explain) \
				VALUES(%s,%s,%s,%s,NOW(),%s)',(title,picture,videourl,author,explain))
	conn.commit()
'''	cur.execute('select video_explain from vl_video where video_id = 40')
	res = cur.fetchone()
	buf = res['video_explain']
	print buf
	if isinstance(buf,unicode):
		buf = buf.encode('utf8')
		print buf
	if isinstance(buf,unicode):
		print '还是unicode编码'
'''
def insertMailRecord(c):
	buf = c.recv(1024)
#	print buf
	sender,receiver,videoFilename,content = buf.split(',')
	videoURL = 'video/' + videoFilename
	cur.execute('insert into vl_mail(sender,receiver,send_time,mail_video,mail_content) VALUES(%s,%s,NOW(),%s,%s)',\
				(sender,receiver,videoURL,content))
	conn.commit()


def recvFile(c):
	fileType,filename = c.recv(24).split(',')
	#根据文件类型觉定文件的保存路径
	path = ''
	if fileType =='video':
		path = r'/var/www/video/'+filename
	else:
		path = r'/var/www/videoimage/'+filename
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

