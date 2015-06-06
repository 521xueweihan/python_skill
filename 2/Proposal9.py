#coding:utf-8
################
# 9数据交换值的时候不推荐使用中间变量
###############
from timeit import Timer

t1 = Timer('temp = x;x = y;y = temp', 'x = 2;y = 3').timeit()
t2 = Timer('x, y = y, x', 'x = 2;y = 3').timeit()

print t1 
print t2 
