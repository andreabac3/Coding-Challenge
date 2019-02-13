#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    k = helper(k)
    return helper(n * k)

def helper(n):
    n = str(n)
    if len(n) == 1:
        return int(n)
    cnt = 0
    for elem in n:
        cnt += int(elem)
    return helper(cnt)  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
