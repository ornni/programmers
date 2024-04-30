import sys
input = sys.stdin.readline

L = int(input())
A = int(input())
B = int(input())
a = int(input())
b = int(input())

days = 0
a_days = 0
b_days = 0

if A % a == 0:
    a_days = A // a
else:
    a_days = (A // a) + 1

if B % b == 0:
    b_days = B // b
else:
    b_days = (B // b) + 1

print(L - max(a_days, b_days))