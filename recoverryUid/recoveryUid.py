# __author__=xk
# -*- coding: utf-8 -*-


import re
from dbConnect import dbConnect


def group(uid):
    return uid[len(uid)-1]

def clean(path):
    wrongFile=open(path,'r')
    if wrongFile:
        uidText = wrongFile.readlines()
        pattern = re.compile(r'[0-9]*@N[0-9]{2}')
        uid=[]
        for line in uidText:
            match=pattern.search(line)
            if match:
                uid.append(match.group())
        wrongFile.close()
        wrongFile = open(path, 'w')
        for i in uid:
            wrongFile.write(i)
            wrongFile.write('\n')
        wrongFile.close()
    else:
        print "File Doesn't Exist"



def maxUid():
    wrongFile = open(r'C:\Users\xk\PycharmProjects\Coding\res\wrong', 'r')
    uid=[]
    uidText=wrongFile.readlines()
    for line in uidText:
        uid.append(line.strip('\n'))
    maxRev=max(uid)
    return maxRev

def minUid():
    wrongFile = open(r'C:\Users\xk\PycharmProjects\Coding\res\logwrong', 'r')
    uid=[]
    uidText=wrongFile.readlines()
    for line in uidText:
        uid.append(line.strip('\n'))
    minRev=min(uid)
    return minRev



def recovery():
    clean(r'C:\Users\xk\PycharmProjects\Coding\res\wrong')
    clean(r'C:\Users\xk\PycharmProjects\Coding\res\logwrong')
    minRevUid=minUid()
    maxRevUid=maxUid()
    g1=group(minRevUid)
    g2=group(maxRevUid)
    conn,cur=dbConnect()
    print minRevUid
    print maxRevUid
    raw_input("Enter AnyKey To StartRecovery~~~")
    if g1 != g2:
        s="UPDATE users_"+str(g1)+" SET FLAG=0 WHERE uid>=%s"
        cur.execute(s,(minRevUid,))
        s="UPDATE users_"+str(g2)+" SET FLAG=0 WHERE uid<=%s"
        cur.execute(s,(maxRevUid,))
        if int(g2)-int(g1)>1:
            for g in range(int(g1)+1,int(g2)):
                s="UPDATE users_"+str(g)+" SET FLAG=0"
                cur.execute(s)
    else:
        s = "UPDATE users_" + str(g1) + " SET FLAG=0 WHERE uid>=%s AND uid<=%s"
        cur.execute(s,(minRevUid,maxRevUid))
    conn.commit()
    cur.close()
    conn.close()
if __name__ == '__main__':
    recovery()