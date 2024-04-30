import sys
input = sys.stdin.readline

n = int(input())
x = len(str(n))

for _ in range(x-1):
    n /= 10

    integer = int(n)
    decimal = n - integer
    
    if decimal >= 0.5:
        n = integer + 1
    else: 
        n = integer
    
print(n * (10**(x-1)))
