#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    value = 0
    step = 0
    lun = len(c)
    for i in range(lun):
        if i != 0 and step != 0:
            step -= 1
        if i == lun - 1:
            return value
        if step == 0 and c[i] == 0:
            value += 1
            if i + 2 < lun:
                if c[i + 2] == 0:
                    step += 2
                    continue
            if c[i + 1] == 0:
                step += 1
        else:
            step -= 1
    return value


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
