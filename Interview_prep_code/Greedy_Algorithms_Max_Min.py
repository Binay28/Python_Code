import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    #sorted(arr)
    #print(arr)
    #subarr=arr[:k]
    arr.sort()
    return(max(arr[:k])-min(arr[:k]))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
#this code is failing 14/17 test cases.
