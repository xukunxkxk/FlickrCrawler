# __author__=xk
# -*- coding: utf-8 -*-
import os
import os.path


def codingCounting(rootDir, *args):
    totalCount = 0
    assert os.path.isdir(rootDir), '%s not exit.' %rootDir
    filList = []
    for root, dirs, files in os.walk(rootDir):
        for filesPath in files:
            filList.append(os.path.join(root, filesPath))

    for fileName in filList:
        totalCount += countingLine(fileName, *args)

    print totalCount

def countingLine(fileName, *args):
    suffix = fileName.split(".")[-1]
    if not suffix in args:
        return 0
    totalLine = 0
    codingFile = open(fileName)
    for line in codingFile.readlines():
        if line != "":
            totalLine +=1
    codingFile.close()
    return totalLine

def writingFile(rootDir, *args):
    wrtitingDir = 'C:\\Users\\xk\\PycharmProjects\\aaa.txt'
    ffff = open(wrtitingDir, "w")
    assert os.path.isdir(rootDir), '%s not exit.' %rootDir
    filList = []
    for root, dirs, files in os.walk(rootDir):
        for filesPath in files:
            filList.append(os.path.join(root, filesPath))
    for fileName in filList:
        writing(fileName, ffff, *args)

def writing(fileName, file, *args):
    suffix = fileName.split(".")[-1]
    if not suffix in args:
        return 0
    totalLine = 0
    codingFile = open(fileName)
    file.write(fileName.split("\\")[-1])
    file.write("\n")
    file.writelines(codingFile.readlines())
    codingFile.close()
    return totalLine

if __name__ == '__main__':
    dir = r"C:\Users\xk\PycharmProjects\spider"
    # codingCounting(dir, "py", "java")
    writingFile(dir, "py")
