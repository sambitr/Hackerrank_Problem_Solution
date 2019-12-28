#!/bin/python3

import math
import os
import random
import re
import sys

"""
A major hint(although not for all test cases) was given at the end of the problem statement by hackerRank. Use that to find the solution.
I used a tad older/brute force approach
"""
# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if (x1 == x2) & (v1 == v2):
        return 'YES'
    elif (x1 == x2) & (v1 > v2):
        return 'NO'
    elif (x1 <= x2) & (v1 <= v2):
        return 'NO'
    else:
        if (x2 - x1) % (v1 - v2) == 0:
            return 'YES'
        else:
            return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
