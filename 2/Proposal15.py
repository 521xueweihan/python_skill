#coding:utf-8
################
# 15.使用enumerate()获取序列迭代的索引和值
###############
"""
前言:如果要对序列进行迭代并获取序列中的元素进行处理的场景。
"""
# 方法1：使用range()和len()方法结合
li = ['a', 'b', 'c', 'd', 'e']
for i in range(len(li)):
    print 'index:',i,'element:',li[i]

print '------------'

# 方法2：使用enumerate()获取序列迭代的索引和值
li = ['a', 'b', 'c', 'd', 'e']
for i,e in enumerate(li):
    print 'index:',i,"element:", e
    
# 笔记：
# 使用enumerate()好，因为他代码简洁，可读性好。
# 而且返回的是一个迭代器。

# 注意：
# 要获取迭代过程中字典的key和value，应该使用iteritems()方法。
    
