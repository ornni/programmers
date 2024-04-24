import sys
input = sys.stdin.readline

def MOD(x, y):
    if y == 0:
        return x
    else:
        return MOD(y, x % y)

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    answer = x * y / MOD(x, y)
    print(int(answer))