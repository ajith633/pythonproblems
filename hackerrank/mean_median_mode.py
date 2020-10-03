# !/bin/python3

import os
import sys
import re
import random
import math
from functools import reduce
from typing import List
import statistics
from collections import Counter




def binmax( num: int) -> int:
    if(num == 0):
        return(num)
    binnum = bin(num)
    return(len(max(re.findall(r'1+',binnum))))

def hourglass(a):
    n=len(a)
    hgsums=[]
    mx=0
    for i in range(n-2):
        for j in range(n-2):
            s=a[i][j]+a[i][j+1]+a[i][j+2]+a[i+1][j+1]+a[i+2][j]+a[i+2][j+1]+a[i+2][j+2]
            if(mx<s):
                mx=s
    return(mx)
def mean(a):
    return(sum(a)/len(a))
def median(a):
    n=len(a)
    ind=n//2
    a.sort()
    if(n%2 == 0):
        return((a[ind]+a[ind-1])/2)
    else:
        return(a[ind])
def mode(a):
    return(Counter(a).most_common(1)[0][0])


if __name__ == '__main__':
    n=int(input())
    arr=list(map(int,input().rstrip().split()))
    print(mean(arr))
    print(median(arr))
    print(mode(arr))





    # Printing result


    #print(my_list)
    #print(*my_list)
    #print(list(zip(*my_list)))
    #print(list(map(sum, zip(*my_list))))
