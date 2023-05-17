#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    answer = ''
    for i in s:
        if i.isalpha():
            k %= 26
            rot = ord(i) + k
            (min, max) = (65, 90) if i.isupper() else (97, 122)
            i = chr(rot) if (min <= rot and rot <= max) else chr(rot - 26)
        answer += i
        
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
