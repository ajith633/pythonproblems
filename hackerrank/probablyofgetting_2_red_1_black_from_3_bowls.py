#!/bin/python3

import math
import os
import random
import re
import sys

import itertools
from fractions import Fraction

X = ["b","b","b","r","r","r","r"]
Y = ["b","b","b","b","r","r","r","r","r"]
Z = ["b","b","b","b","r","r","r","r"]

r = [i for i in itertools.product(X,Y,Z)]

print(r)
#e = list(map(lambda x : x.count('r') == 2 and x.count('b') == 1,r))
e = [i.count('r') == 2 for i in r]
print(e)
print(Fraction(e.count(True),len(e)))


