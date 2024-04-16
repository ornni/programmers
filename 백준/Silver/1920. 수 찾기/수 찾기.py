import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
n_number = list(map(int, input().split()))
n_number.sort()

m = int(input())
m_number = list(map(int, input().split()))

for target in m_number:
    find = False
    start = 0
    end = n-1
    while start <= end:
        median = int((start + end)/2)
        median_number = n_number[median]
        if median_number > target:
            end = median -1
        elif median_number < target:
            start = median + 1
        else:
            find = True
            break

    if find:
        print(1)
    else:
        print(0)