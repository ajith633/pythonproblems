#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    position=[]
    sorted=list(dict.fromkeys(ranked))
    current_pos=len(sorted)-1
    print(sorted)

    for i in player:
        for j in range(current_pos, -1, -1):
            print(i,j, sorted[j])
            if (i < sorted[j]):
                current_pos=j
                position.append(current_pos + 2)
                break
        else:
            position.append(1)
    return(position)

if __name__ == '__main__':

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print('\n'.join(map(str, result)))
