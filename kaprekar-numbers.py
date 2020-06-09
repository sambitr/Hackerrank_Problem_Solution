#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    results = []
    for i in range(p, q+1):
        sqr = str(i ** 2)
        n = len(sqr)
        
        right = sqr[len(sqr)//2:]
        
        if sqr[:len(sqr)//2] == '':
            left = '0'  
        else:
            left = sqr[:len(sqr)//2]
        
        if i == 1:
            results.append(i)
        elif i > 1 and int(left) + int(right) == i:
            results.append(i)

    if len(results) == 0:
        print("INVALID RANGE")
    else:
        print(" ".join(str(x) for x in results))


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
