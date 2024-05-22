import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(n+1):
    parent[i] = i

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a

def check(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return True
    return False

for i in range(m):
    question, a, b = map(int, input().split())

    if question == 0:
        union(a, b)
    else:
        if check(a, b):
            print("YES")
        else:
            print("NO")