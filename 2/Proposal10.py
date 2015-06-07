#coding:utf-8
################
# 10.充分利用Lazy evaluation的特性
###############
# lazy evaluation被称为延时计算，指的是仅仅在真正需要执行的时候
# 才计算表达式的值，好处体现在一下两个方面

# 1.避免不必要的计算，带来性能上的提升
from time import time
from itertools import islice
# 判断一个单词是不是指定的缩写形式
t = time()
abbreviations = ['cd.', 'e.g', 'ex.', 'etc.', 'fig.', 'i.e.', 'Mr', 'vs.']
for i in xrange (1000000):
    for w in ('Mr.', 'Hat', 'is', 'chasing', 'the', 'black', 'cat', '.'):
        if w in abbreviations: # 1.432502985
        # 表达式 x and y,当x为flases 表达式结果就为flase（and后面就不需要计算了）
        # 表达式x or y,当x为true 表达式的结果就为true
        #if w[-1] == '.' and w in abbreviations: # 1.10134792328
            pass
print "用时："
print time()-t

for w in ('Mr.', 'Hat', 'is', 'chasing', 'the', 'black', 'cat', '.'):
    print w[-1]
    
# 2.节省空间，使得无限循环的数据结构成为可能
def fib():
    a, b =0, 1
    while True:
        yield a
        a, b =b, a+b
print list(islice(fib(), 4))# 数字代表列表长度
# 笔记
# 1.如果对于or条件表达式应该将值为真可能性较高的变量写在or的前面，and则应该退后

