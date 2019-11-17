#!/usr/bin/env python
# -*- coding:utf-8 -*-

#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
This module provide ……

Author: zhanglu(zhanglu34@baidu.com)
Date: 2019/11/16 22:28
@File: traversal.py
"""
import sys, importlib

importlib.reload(sys)

query = {
    "是的": "yes",
    "你好": "hello",
    "再见": "byebye"
}

for x, y in query.items():
    print(x, y)