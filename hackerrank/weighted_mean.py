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


def weightedmean(X,W,n):
    s=sum([x*y for x,y in (zip(X,W))])
    by=sum(W)
    return(round(s/by,1))

if __name__ == '__main__':
    n=int(input())
    X=list(map(int,input().rstrip().split()))
    W=list(map(int,input().rstrip().split()))
    print(weightedmean(X,W,n))





    # Printing result


    #print(my_list)
    #print(*my_list)
    #print(list(zip(*my_list)))
    #print(list(map(sum, zip(*my_list))))
