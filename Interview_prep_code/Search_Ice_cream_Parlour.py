import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    for i in range(len(cost)):
        if(money-cost[i] in cost[i+1:]):
            print(cost.index(cost[i])+1,cost.index(money-cost[i])+1)
            break
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
#this code is failing 1/3 sample test cases and all the test cases.
#def get_flavours(money,flavours):
#    map = {}
#    for pos, cost in enumerate(flavours):
#        if cost in map:
#            return (map[cost], pos + 1)
#        else:
#            map[money-cost] = pos + 1
#this is not my code.
