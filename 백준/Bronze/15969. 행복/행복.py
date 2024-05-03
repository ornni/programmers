import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

a = min(A)
b = max(A)
        
print(b-a)
