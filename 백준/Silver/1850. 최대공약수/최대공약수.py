import sys
input = sys.stdin.readline

def MOD(x, y):
    a = max(x, y)
    b = min(x , y)
    if b == 0:
        return a
    else:
        return MOD(b, a % b)

n, m = map(int, input().split())

answer = MOD(n, m)

while answer > 0:
    print(1, end = '')
    answer -= 1