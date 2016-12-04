# __author__=xk
# -*- coding: utf-8 -*-


# 列表解析
import os

ls = os.linesep  # 行分割符
l = list()
for i in range(10):
    l.append(i)
file = open('my.txt', 'w')
file.writelines(['%s%s' % (x, ls) for x in l])  # 列表解析

# random 模块
# randint(flickrApi,b) randrange(flickrApi,b)

# 字典
dic = {}.fromkeys(('x', 'y'), -1)
dic.items()  # 返回键值对

# 时间
import datetime

print datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# md5
import hashlib

src = "1111"
m2 = hashlib.md5()
m2.update(src)
print m2.hexdigest()

if __name__ == '__main__':
    pass
