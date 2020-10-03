#!/bin/python3

import math
import os
import random
import re
import sys


def findmedian(a):
    n=len(a)
    if(n%2==0):
        med=(a[n//2]+a[n//2-1])/2
    else:
        med=a[n//2]
    return(med)
def findquartiles(a):
    n=len(a)
    if(n%2==0):
        return(findmedian(a[n//2:])-findmedian(a[:n//2]))
    else:
        return(findmedian(a[n//2+1:])-findmedian(a[:n//2]))


if __name__ == '__main__':
    n=int(input())
    X=list(map(int,input().rstrip().split()))
    F=list(map(int,input().rstrip().split()))
    S=[]
    for i in range(n):
        S+=[X[i]]*F[i]
    S.sort()
    print(round(findquartiles(S)+0.0,1))



