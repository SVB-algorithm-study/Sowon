#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    arr.sort()
    length = len(arr)
    min = sys.maxsize
    
    ans_arr = []
    for i in range(length):
        if i != length-1:
            diff = arr[i+1] - arr[i]
            if min > diff:
                min = diff
                ans_arr = [arr[i], arr[i+1]]
            elif min == diff:
                ans_arr.append(arr[i])
                ans_arr.append(arr[i+1])
    return ans_arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
