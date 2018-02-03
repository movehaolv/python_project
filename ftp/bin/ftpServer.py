#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : haolv

import sys,os

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

from core import socket_server

if __name__ == "__main__":
    HOST,PORT = "localhost",9901
    server = socket_server.socketserver.ThreadingTCPServer((HOST,PORT),socket_server.MyTCPServer)
    server.serve_forever()