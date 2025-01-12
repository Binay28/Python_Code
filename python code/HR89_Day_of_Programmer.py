import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if(year==1918):return(".".join(["26","09","1918"]))
    elif(year<=1917):
        if(year%4==0): return(".".join(["12","09",str(year)]))
        else: return(".".join(["13","09",str(year)]))
    elif(year>=1919):
        if(year%400==0 or (year%4==0 and year%100!=0)):return(".".join(["12","09",str(year)]))
        else:return(".".join(["13","09",str(year)]))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
#In the year 1918 the 256th day is 26th and not 27th that's why one of the test cases was failing.
