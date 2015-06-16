#coding:utf-8
################
# 14.警惕eval()的安全漏洞
###############
"""
前言:eval()函数将字符串当成有效的表达式来求值并返回计算结果。 
    但是eval函数有安全问题。
"""

print "什么是eval(),看下面的例子,注意：表达式要用''或""(表示为字符串)："
print eval("1+1 == 2")
print eval('1 + 2')
print eval("'A' + 'B'")

# eval()函数是邪恶的，他可以执行"__import__("os").system("dir")"——显示当前的文件列表
# 然后，入侵者还可以用类似的字符串删除你的文件，太可怕了！

# 结论
# 所以，如果使用对象不是信任源，应该尽量避免使用eval，在需要的使用eval的地方可以用安全性
# 更好的 ast.literal_eval替代。