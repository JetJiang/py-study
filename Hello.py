# 单引号输出一行
print('Hello,Python')


# 如果要输出多行，可以这样'''
print('''Hello
Python,
I'm coming
''')

a = 100
if a > 0:
    print(a)
else:
    print(-a)

# 计算字符数
print(len('中国'))

# 计算字节数
print(len('中国'.encode('utf-8')))

# 格式化字符串，占位符的使用
print('hello %s,你%d月份的水费是 %.2f 元,比上个月提升了20%%' % ('李明', 7, 99.6))
