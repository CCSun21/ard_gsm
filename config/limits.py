#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 按照文献要求修改价键限制
# First number is the minimum number of connections;
# second number is the maximum number of connections.
connection_limits = {
    'H': (1, 1),   # 氢原子必须有一个键
    'C': (2, 4),   # 碳原子最少2个键,最多4个键
    'N': (1, 3),   # 氮原子最少1个键,最多3个键
    'O': (1, 2),   # 氧原子最少1个键,最多2个键 
}
