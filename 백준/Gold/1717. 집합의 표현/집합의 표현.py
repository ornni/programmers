import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = []

for i in range(n+1):
    parent.append(i)

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a != b:
        parent[b] = a

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
    
def checksame(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return True
    else:
        return False
    
for _ in range(m):
    q, a, b = map(int, input().split())

    if q == 0:
        union(a, b)
    else:
        if checksame(a, b):
            print("YES")
        else:
            print("NO")