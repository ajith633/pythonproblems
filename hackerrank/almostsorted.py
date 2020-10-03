#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the almostSorted function below.
def almostSorted(arr):
    n=len(arr)
    low=n-1
    high=0
    i=0
    j=n-1
    if(n==2 and arr[0]>arr[1]):
        print('yes')
        print('swap 1 2')
        return()
    for i in range(n-1):
        if(arr[i]>arr[i+1]):
            low=i
            break
    else:
        print('yes')
        return()
    #Now you know the index of first element that would break the ascending order
    for j in range(n-1,0,-1):
        if(arr[j]<arr[j-1]):
            high=j
            break
    #Now you also the index of the first element from backwards that would break the descending order
    print('i={} and j={}'.format(i,j))
    for k in range(i,j+1):
        if(arr[k]<arr[k+1]):
            print('no')
            break
    if((arr[i]>arr[j]) or (j>0 and arr[i]>arr[j-1]) or (i<n-1 and arr[i+1]>arr[j])):
        print('no')
        return()



    if((j-i)==2):
        print('swap',i+1,j+1)
    else:
        print('reverse',i+1,j+1)

'''
    phase=0
    dsc=0
    asc2=0
    high=0
    loc=[]
    for i in range(len(arr)-1):
        if(phase==0):
            if (arr[i]<arr[i+1]):
                high=arr[i+1]
            else:
                phase=1
                loc.append(i+1)
        elif(phase==1):
            if(arr[i]>arr[i+1]):
                loc.append(i+1)
            elif(arr[i+1]>high):
                phase=2
                loc.append(i+1)
                high=arr[i+1]
            else:
                print('no')
                return()
        else:
            if(arr[i]>arr[i+1]):
                print('no')
                return()
    if(len(loc)==1 and len(arr)==2):
        loc.append(len(arr))
        print('swap',loc)

    elif(len(loc)==2):
        print('swap',loc)
    else:
        print('yes',*loc)

'''
def printyes(s,sr,a,b):
    print(s)
    print(sr,a+1,b+1)

def printyesno(s):
    print(s)

def alreadysorted(arr):
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

    #almostSorted(arr)
    alreadysorted(arr)
