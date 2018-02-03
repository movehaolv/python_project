#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : haolv

import os,sys
path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(path)

from core import socket_client

if __name__ == "__main__":
    host,port = "localhost",9901
    myClient = socket_client.MySocketClient(host,port)
    myClient.start()

