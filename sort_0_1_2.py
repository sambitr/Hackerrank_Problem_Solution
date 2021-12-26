# https://www.codingninjas.com/codestudio/problems/sort-0-1-2_631055?source=youtube&campaign=LoveBabbar_Codestudiovideo1&utm_source=youtube&utm_medium=affiliate&utm_campaign=LoveBabbar_Codestudiovideo1&leftPanelTab=0
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)


def sort012(arr, n):
    # write your code here
    # don't return anything
    c0,c1,c2 = 0,0,0
    final_arr = []
    for i in range(n):
        if arr[i] == 0 :
            c0 += 1
        if arr[i] == 1 :
            c1 += 1
        if arr[i] == 2 :
            c2 += 1

    j = 0
    while(c0 > 0):
        arr[j] = 0
        j+=1
        c0-=1

    while(c1 > 0):
        arr[j] = 1
        j+=1
        c1-=1

    while(c2 > 0):
        arr[j] = 2
        j+=1
        c2-=1

    return(arr)
    pass


# taking inpit using fast I/O
def takeInput():
    n = int(input().strip())

    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


def printAnswer(arr, n):
    for i in range(n):
        print(arr[i], end=" ")

    print()


# main

t = int(input().strip())
for i in range(t):
    arr, n = takeInput()
    sort012(arr, n)
    printAnswer(arr, n)

