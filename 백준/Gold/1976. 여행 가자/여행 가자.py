import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

city= [[0 for j in range(n+1)] for i in range(n+1)]

for i in range(1, n+1):
    city[i] = list(map(int, input().split()))
    city[i].insert(0, 0)

route = list(map(int, input().split()))
route.insert(0, 0)

parent = []
for i in range(n+1):
    parent.append(i)

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

for i in range(1, n+1):
    for j in range(1, n+1):
        if city[i][j] == 1:
            union(i, j)

index = find(route[1])
isconnected = True

for i in range(2, len(route)):
    if index != find(route[i]):
        isconnected = False
        break

if isconnected:
    print("YES")
else:
    print("NO")