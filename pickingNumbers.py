#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    count = []
    a.sort()
    maximum = 0
    for i in range(len(a)-1, -1, -1):
        count = 1
        for j in range(i-1, -1 , -1):
            if (a[i]-a[j]) < 2:
                count+=1
        if count > maximum:
            maximum = count
        else:
            maximum = maximum

    return maximum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
