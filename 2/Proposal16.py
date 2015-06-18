#coding:utf-8
################
# 16.分清 == 与is的适用的场景
###############
"""
前言:is的作用是用来检查队形的标示符是否一致的，也就是比较两个对象在内存中
是否拥有同一块内存空间，他并不适合用来判断两个字符串是否相等。x is y相当于
id(x) == id(y)
    而 == 才是用来检验两个对象的值是否相等。
"""
#  判断两个对象相等应该使用 == 而不是is
a = 'Hi'
b = 'Hi'
print a is b  # True
print a == b  # True

a1 = "I am using long string for testing"
b1 = "I am using long string for testing"
print id(a1)
print id(b1)
print a1 is b1  # True 和书上的结果不一样
print a1 == b1  # True

str1 = "string"
str2 = ''.join(['s', 't', 'r', 'i', 'n', 'g'])
print str1 is str2  # Flase
print str1 == str2  # True


# 笔记
#
# python中的（字符串驻留机制）
# 对于较小的字符串，为了提高系统性能会保留其值的一个副本，
# 当创建新的字符串的时候直接指向该副本即可。
# 而长字符串，并不会驻留，Python在内存中各自创建了对象来表示
# 长字符串，这两个兑现拥有相同的内容但对象标识符却不相同。
#
#
#


