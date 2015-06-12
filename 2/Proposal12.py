#coding:utf-8
################
# 12.不推荐使用type来进行类型检查
###############
"""
前言:python作为动态性脚本语言，变量在定义时不需要指明具体类型。
    为了充分利用其动态特征是不推荐进行类型检查的。如果两者之间，
    类型不同又不能进行隐式类型转换（类如int+double转成double）
    便抛出TypeError异常
"""
import types
def add(a, b):
    return a+b
    
print add(3, 4.1)  #隐式类型转换
# 不刻意进行类型检查，而是在出错的情况下通过抛出异常来进行处理。
#print add(5, 'a')  #抛出TypeError异常


# 如果为了提高程序的健壮行，面临需要进行类型检查的情景。
# 使用下面的方法进行，类型检查

list1 = []
if type(list1) is types.ListType: #通过python自带的模块types中定义的名字进行比较
    print 'list1 is List'

# 下面是使用type进行变量类型检查，会出现问题的两个示例：

# 示例1：
class TestInt(int):  #TestInt类继承自int类
    pass  # 什么都不做，不会报错

n = TestInt()    
print type(n) is types.IntType #Flase
# 由此可见基于内建类型扩展的用户自定义类型，type函数并不能准确返回结果

# 示例2：
class A:
    pass
    
class B:
    pass

a = A()
b = B()

print type(a) == type(b)  #True

# 这里有个疑问：如果我写成class A(object) 和class B(object)
# 之后输出type(a) == type(b) 结果是Flase 为什么？


# 使用isinstance()函数来解决以上两个示例：
# isinstance()函数支持多种类型那个列表
print isinstance(n, TestInt) # 这样就可以正确的显示34行的代码的类型了：True
# 子类是的type等于父的，但是父类的不等于子类的






  
  
