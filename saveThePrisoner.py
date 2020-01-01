#!/bin/python3

import math
import os
import random
import re
import sys

"""
In this problem, we need to determine the ID of last prisoner which can be done by moving M-1 steps further from S.
ID of last prisoner= (M-1+S)
Since we are moving in a circle so we need to take mod of this summation with N.
Because the ID starts from 1, so the ID of last prisoner= (M – 1 + S – 1) % N + 1)
"""
# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    value = (n+m+s-1)%n
    if value == 0:
        return n
    else:
        return value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
