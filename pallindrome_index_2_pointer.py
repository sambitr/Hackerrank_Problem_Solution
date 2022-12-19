## https://www.hackerrank.com/challenges/palindrome-index/problem?h_r=internal-search

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    # Write your code here
    # 2 pointer problem solution
    i = 0
    j = len(s)-1
    
    while (i < j):
        if s[i] != s[j]:
            if s[i+1] == s[j] and s[i+2] == s[j-1]:
                return i
            else:
                return j
        i+=1
        j-=1
        
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
