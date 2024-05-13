import sys
input = sys.stdin.readline

n = int(input())
A = [[0]*2 for _ in range(n)]

for i in range(n):
    s, e = map(int, input().split())
    A[i][0] = e
    A[i][1] = s
    
A.sort()
count = 0
end = -1

for i in range(n):
    if A[i][1] >= end:
        end = A[i][0]
        count += 1

print(count)