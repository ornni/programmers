import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A = [[] for _ in range(m)]
X = list(range(1, n+1))

for i in range(m):
    s, e = map(int, input().split())
    A[i].append(s)
    A[i].append(e)

for i in A:
    R = X[i[0]-1 : i[1]]
    R.reverse()
    X[i[0]-1 : i[1]] = R 

print(*X)