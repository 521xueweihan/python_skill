#coding:utf-8
################
# 11.理解枚举替代实现的缺陷
###############
"""
前言：枚举有很多的替代方法，但是或多或少都有一些缺陷，
      python2.7支持第三方模块flufl.enum，(可以通过pip安装)是实现枚举
      不错的选择。
"""
from flufl.enum import Enum
# 继承自Enum定义枚举,枚举值唯一
#class Seasons(Enum):
#    Spring = 'Spring' #如果给spring赋值2，报错
#    Summer = 2 
#    Autumn = 3
#    Winter = 4

# 直接实例化Enum类
Seasons = Enum('Seasons', 'Spring Summer Autumn Winter')   

# flufl.enum 提供了__members__属性，可以对枚举名称进行迭代 
for member in Seasons.__members__:
    print member
    
#可以直接使用value属性获取枚举元素的值
print "Summer的值为："
print Seasons.Summer.value




    
