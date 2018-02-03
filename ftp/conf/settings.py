#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : haolv

import os,sys

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#用户家目录
HOMEPATH = os.path.join(BASEDIR,"home")

#数据库目录
DATABASE = os.path.join(BASEDIR,"database")

#分给没个用户的磁盘配额
LIMITSIZE = 20480000

#用户从服务端下载文件的默认地址
DEFAULT_PATH = "E:\\myGitHup\\python\\ftp\\download"

