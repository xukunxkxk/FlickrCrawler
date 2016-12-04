# __author__=xk
# -*- coding: utf-8 -*-
from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inX, dataSet, labels, k):
    # shape查看矩阵或数组的维数
    dataSetSize = dataSet.shape[0]
    # 欧式距离计算
    # tile(A, (m, n))将数A作为元素构造出m*n的数组
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffmat = diffMat ** 2
    # arrys.sum(axis=1)按行累加
    sqDistances = sqDiffmat.sum(axis=1)
    distances = sqDistances ** 0.5
    # argsort得到矩阵中每个元素排序序号
    sortedDistIndicies = distances.argsort()
    classCount = {}
    # 前K个元素
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def file2martix(filename):
    fr = open(filename)
    arrayOflines = fr.readlines()
    numberOfLines = len(arrayOflines)
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOflines:
        line = line.strip()
        listFromFile = line.split('\t')
        returnMat[index, :] = listFromFile[0: 3]
        classLabelVector.append(int(listFromFile[-1]))
        index += 1
    return returnMat, classLabelVector


if __name__ == '__main__':
    # group, labels = createDataSet()
    # print classify0([0,0], group, labels, 3)
    datingfDataMat, datingLabels = file2martix("datingTestSet2.txt")
    flg = plt.figure()
    ax = flg.add_subplot(111)
    ax.scatter(datingfDataMat[:, 1], datingfDataMat[:, 2], 15.0 * array(datingLabels), 15.0 * array(datingLabels))
    plt.show()
