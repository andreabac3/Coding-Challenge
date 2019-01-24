#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):
    lun = len(s)
    value = 0
    for char in s:
        if char == 'a': value += 1
    value *= (n // lun)
    for i in range(n % lun):
        if s[i] == 'a': value += 1
    return value


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
