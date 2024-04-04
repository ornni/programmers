import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

A.sort()

cum = []
cum_num = 0
for i in A:
    cum_num += i
    cum.append(cum_num)

print(sum(cum))