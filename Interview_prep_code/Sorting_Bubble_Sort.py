import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    count=0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if(a[j]>a[j+1] and j!=len(a)-1):
                s=a[j]
                a[j]=a[j+1]
                a[j+1]=s
                count+=1
    print("Array is sorted in",count,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])
if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
#should think another way to count the number of swaps instead of actually doing bubble sort.
