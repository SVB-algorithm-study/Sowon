#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    max_first = len(s)//2
    is_find = -1
    
    for i in range(1, max_first+1):
        first = s[:i]
        sen = ''
        j = 0
        while len(sen + str(int(first) + j)) <= 32:
            sen += str(int(first) + j)
            if sen == s:
                is_find = first
                break
            j += 1
    
    print('YES ' + is_find if is_find != -1 else 'NO')

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
