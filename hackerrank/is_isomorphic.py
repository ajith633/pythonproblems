import sys
import itertools
from fractions import Fraction
from collections import defaultdict


def isIsomorphic(s: str, t: str) -> bool:
    #d=dict([(x,0) for x in s])
    d = dict.fromkeys(s, 0)
    for i, j in zip(s, t):
        if (d[i] == 0):
            if (j in d.values()):
               return (False)
            d[i] = j
        elif (d[i] != j):
            return (False)
    return(True)
if __name__ == '__main__':
    print(isIsomorphic('paper','title'))
    print(isIsomorphic('foo','bar'))
    print(isIsomorphic('ab','aa'))
    print(isIsomorphic('aa','ab'))


