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

def signin(connect):pass
def offine(conn):pass
def video(c):pass
def videoinfo(c):pass
def mailinfo(c):pass
def close(c):pass

