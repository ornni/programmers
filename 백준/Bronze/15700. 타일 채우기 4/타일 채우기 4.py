import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

answer = n * m // 2

print(answer)