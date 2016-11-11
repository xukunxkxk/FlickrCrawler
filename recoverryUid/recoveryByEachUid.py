# __author__=xk
# -*- coding: utf-8 -*-
# __author__=xk
# -*- coding: utf-8 -*-


import re
from dbConnect import dbConnect



def group(uid):
    return uid[len(uid)-1]

# def clean(path):
#     wrongFile=open(path,'r')
#     if wrongFile:
#         uidText = wrongFile.readlines()
#         pattern = re.compile(r'[0-9]*@N[0-9]{2}')
#         uid=[]
#         for line in uidText:
#             match=pattern.search(line)
#             if match:
#                 uid.append(match.group())
#         wrongFile.close()
#         wrongFile = open(path, 'w')
#         for i in uid:
#             wrongFile.write(i)
#             wrongFile.write('\n')
#         wrongFile.close()
#     else:
#         print "File Doesn't Exist"

def clean(path):
    uidIsDuplicatedDict = {}
    with open(path, 'r') as wrongFile:
        pattern = re.compile(r"\**Uid ([0-9]*@N[0-9]{2}) Didn't have followers")
        for i in wrongFile.readlines():
            match = pattern.match(i)
            if match:
                uid = match.groups()[0]
                if not uidIsDuplicatedDict.has_key(uid):
                    uidIsDuplicatedDict[uid] = 1
    if len(uidIsDuplicatedDict):
        with open(path, 'w') as wrongFile:
            for uid in uidIsDuplicatedDict.keys():
                wrongFile.write(uid)
                wrongFile.write('\n')


def recovery():
    conn,cur=dbConnect()
    clean(r'C:\Users\xk\PycharmProjects\Coding\res\eachUid')
    wrongFile = open(r'C:\Users\xk\PycharmProjects\Coding\res\eachUid', 'r')
    data=wrongFile.readlines()
    #raw_input("Enter AnyKey To StartRecovery~~~")
    for line in data:
        uid=line.strip('\n')
        g=group(uid)
        s="UPDATE users_"+str(g)+" SET FLAG=0 WHERE uid=%s"
        cur.execute(s, (uid,))
        print uid
    conn.commit()
    cur.close()
    conn.close()
if __name__ == '__main__':
    recovery()

