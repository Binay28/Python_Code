import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    count=0
    for i in arr:
        count+=arr.count(i+k)
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
#this code is failing 5/17 test cases due to timeout.
#could sort the array and change the loop to go to <=max(arr)-k element. 
