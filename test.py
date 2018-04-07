#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
------------------------------------------------------
    Project : TongmingClient
    File    : test.py 
    Time    : 2018/02/02 
    Author  : liulijun
    Site    : https://github.com/markliu666/
------------------------------------------------------
"""
# test.py
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"] # python3
    #return ["Hello World"] # python2