import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    ls=list()
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):ls.append(abs(arr[i]-arr[j]))
    return min(ls)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
#this code is failing 4/10 testcases due to timeout. Testcase numbering starts from 0.