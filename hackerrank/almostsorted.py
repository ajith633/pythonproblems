#!/bin/python3

import math
import os
import random
import re
import sys
'''
# Complete the almostSorted function below.
https://www.hackerrank.com/challenges/almost-sorted/problem
Given an array of integers, determine whether the array can be sorted in ascending order using only one of the following operations one time.

Swap two elements.
Reverse one sub-segment.
Determine whether one, both or neither of the operations will complete the task. If both work, choose swap. For instance, given an array  either swap the  and , or reverse them to sort the array. Choose swap. The Output Format section below details requirements.

'''

def printyes(s,sr,a,b):
    print(s)
    print(sr,a+1,b+1)

def printyesno(s):
    print(s)

def almostsorted(arr):
    n=len(arr)
    if(n==2):
        if(arr[0]<arr[1]):
            printyesno('yes')
        else:
            printyes('yes','swap',0,1)
        return()
    phase=0
    p1=v1=p2=v2=-1
    for i in range(n-1):
        if(phase==0):
            if(arr[i]>arr[i+1]):
                p1=i
                phase=1
            #else: continue
        elif(phase==1):
            if(arr[i]<arr[i+1]):
                v1=i
                phase=2
            # else: continue
        elif(phase==2):
            if(arr[i]>arr[i+1]):
                p2=i
                phase=3
        elif(phase==3):
            if (arr[i] < arr[i + 1]):
                v2=i
                phase=4
        else:
            if(arr[i]>arr[i+1]):
                print('no')
                return()

    #END OF FOR
    print(phase,i,p1,v1,p2,v2)
    if(p1<0):
        #Fully storted array, No need to do anything
        printyes('yes')
    if(v1<0):
        v1=n-1
        if(v1-p1 > 2):
            if(arr[p1-1]<arr[v1]):
                printyes('yes','reverse',p1,v1)
            else:
                printyes('no')
        else:
            printyes('yes','swap',p1,v1)
        return()


    elif(p2<0):
        if((p1==0 or arr[p1-1]<arr[v1]) and (arr[p1]<arr[v1+1])):
            if(v1-p1>2):
                printyes('yes','reverse',p1,v1)
            else:
                printyes('yes','swap',p1,v1)
        else:
            printyesno('no')
        return()
    elif(v2<0):
        v2=n-1

    if(arr[p1] < arr[v2-1]):
        printyesno('no')
        return ()
    if(p1!=0 and arr[v2]<arr[p1-1]):
        printyesno('no')
        return ()
    if(v2!=n-1 and arr[p1]>arr[v2+1]):
        printyesno('no')
        return ()
    if(arr[v2]>arr[p1+1]):
        printyesno('no')
        return ()
    printyes('yes','swap',p1,v2)




if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    almostSorted(arr)
