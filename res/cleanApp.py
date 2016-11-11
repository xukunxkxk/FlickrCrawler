# __author__=xk
# -*- coding: utf-8 -*-


#格式化myApp
if __name__ == '__main__':
    try:
        file = open(r'C:\Users\xk\PycharmProjects\Coding\res\myApp','r')
        data = file.readlines()
        file.close()
        file = open(r'C:\Users\xk\PycharmProjects\Coding\res\myApp','w')
        file.truncate()
        result=[]
        for i in data:
             #去除空格与文字key
            if i.strip() and i!='密鑰：\n' and i!='key：\n':
                result.append(i)
        file.writelines(result)
        print "App Clean Over"
    except IOError as e:
        print e