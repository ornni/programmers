import sys
input = sys.stdin.readline

n = int(input())
A =[]

for i in range(n):
    A.append(int(input()))

A.sort()

for num in A:
    print(num)