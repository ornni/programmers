import sys
input = sys.stdin.readline

a, b = map(int, input().split())

def GCD(a, b):
    x = max(a, b)
    y = min(a, b)
    
    if y == 0:
        return x
    else:
        return GCD(b, a%b)

gcd = GCD(a, b)

for _ in range(gcd):
    print(1, end = '')

