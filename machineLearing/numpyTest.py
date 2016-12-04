# __author__=xk
# -*- coding: utf-8 -*-
from numpy import *

if __name__ == '__main__':
    randMat = mat(random.rand(4, 4))
    randMatInverse = randMat.I
    mul = randMatInverse * randMat
    print mul
