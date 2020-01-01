#!/bin/python3

import math
import os
import random
import re
import sys

##Explanation at the end
# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    commonLength = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            commonLength+=1
        else:
            break

    if (len(s)+len(t)-2*commonLength)>k:
        return 'No'
    elif (len(s)+len(t)-2*commonLength)%2 == (k%2):
        return 'Yes'
    elif (len(s)+len(t)-k) < 0:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()




"""
CASE A:
What this case is finding is if k is bigger than the difference in length of the two strings.

example: s = "123456789", t = "1", k = 5

in this case, you definitely need a bigger k to transform s to t or vice versa, therefore you reject any such cases.

Case B:
now that the case has passed A, we can say that the total number of letters required to change is less than or equal to k.

however the next problem comes because the question specified that exactly k moves must be done, no more no less. this leads to an example whereby:

s = "010101", t = "01010", k = any EVEN number

OR

s = "010101", t = "010101", k = any ODD number

from these two examples you can see that only if k is odd/even matches the odd/even of number of different digits will such cases pass.

Case C:
However there is a way to overcome this odd/even problem if you are able to completely delete away one string as a deletion action on an empty string results in another empty string.

Example: s = '1' t = '101' k = 5

in this case, to get a S from T you could do delete-delete-delete-delete-add(1) and you will satisfy the condition.

Case D:
all other cases will fail the test
"""
