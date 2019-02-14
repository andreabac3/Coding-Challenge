#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    competition = []
    cnt = 0
    for contest in contests[0:]:
        if contest[1]:
            competition.append(contest[0])
        cnt += contest[0]
    diff = len(competition) - k
    for i in range(diff):
        minimo = min(competition)
        cnt -= (minimo)*2
        competition.remove(minimo)
    return cnt





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()

