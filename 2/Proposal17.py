#coding:utf-8
################
# 17.考虑兼容性，尽可能使用Unicode
###############
"""
前言:Python内建的字符串有两种类型：str和Unicode，因为最早的ASCII编码使用一个字节
只能表示128个字符，但是对于很多语言128个字符数远远不够，这个时候出现了多种编码格式
从而导致不同平台，不同语言之间的文本无法进行很好地转换。
    要解决这个问题，必须为不同的文字分配统一的编码，Unicode，也被称为‘万国码’。
"""
#####
# 场景1:读取文件显示乱码

filehandle = open("test.txt", 'r')  # 读取测试中文文件‘test.txt’
print filehandle.read()
filehandle.close()  #关闭资源

# 因为：文本的编码为UTF-8，但是windows系统中他被映射为GBK编码，所以在运行之后，
# 两种编码并不兼容。
# Unicode 为不同语言设置了唯一的二进制表表示形式（方便于相互转化）
#####

# 解决办法：使用decode()和encode()方法，分别是解码和编码

filehandle = open("test.txt", 'r')  # 读取测试中文文件‘test.txt’
# 这里decode()方法将其他编码对应的字符串解码成Unicode，
# encode()方法将Unicode编码转换为另一种编码，Unicode作为中间编码
print (filehandle.read().decode("UTF-8")).encode("gbk")
filehandle.close()  #关闭资源


#####
# 场景2：输出中文字符，抛出异常SyntaxError

print '中文测试'

# 因为：Python中默认的编码是ASCII编码，包含中文的字符串。当调用print输出时
# 采用隐式地进行从ASCII到系统默认编码的转换，中文字符并不是ASCII字符，此时
# 源文件又未指定其他编码方式，这时便会抛出SyntaxError异常
#####
# 解决办法：在源文件中进行编码声明，
# 如：#coding=utf-8

print '中文测试'


#####
# 场景3：普通字符串和Unicode进行字符串连接时抛出UnicodeDecodeError异常

print '中文测试' + u'Chinese Test' #抛出异常

# 因为：当两种类型的字符串连接的时候，Python将左边的中文字符串转换为
# Unicode再与右边的Unicode字符串连接，这时将‘中文测试’字符串转换为Unicode
# 使用系统默认的ASCII编码对字符串进行解码，但是其中‘中’字对应的值为214，
# 当编码值在0～127的时候Unicode和ASCII是兼容的，但是大于128的时候，ASCII编码
# 不能正确处理这种情况，则抛出异常
#####
# 解决办法：把中文字符解码成gbk编码
print '中文测试'.decode('gbk') + u'Chinese Test' 


# 笔记
# 对于中文字符，为了做到不同系统之间的兼容，建议使用Unicode方式表示。
# Python2.6之后可以通过import unicode_literals自动将定义的普通字符
# 识别为Unicode字符串,这样字符串的行为将和Python3中保持一致。

# 形式如下：

#from __future__ import unicode_literals
s = '中文测试'
print s




















