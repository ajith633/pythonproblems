import sys
import itertools
from fractions import Fraction
from collections import defaultdict


def sumOddLengthSubarrays(arr) -> int:
    n = len(arr)
    tot = 0
    # For all odd numbers
    for i in range(1, n+1, 2):
        for j in range(0,n+1-i):
            #print(arr[j:j+i])
            tot+=sum(arr[j:j+i])
    return(tot)


if __name__ == '__main__':
    print(sumOddLengthSubarrays([1,4,2,5,3]))

    print(sumOddLengthSubarrays([1,2,3,4,5,6]))

    print(sumOddLengthSubarrays([6]))

