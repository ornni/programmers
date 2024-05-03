import sys
input = sys.stdin.readline

n = int(input())

def GCD(a, b):
    x = max(a, b)
    y = min(a, b)
    
    if y == 0:
        return x
    else:
        return GCD(b, a%b)

for _ in range(n):
    a, b = map(int, input().split())
    gcd = GCD(a, b)
    print(int(a * b / gcd))
