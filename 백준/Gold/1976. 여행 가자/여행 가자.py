import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
city = [[0 for _ in range(n+1)] for _ in range(n+1)]

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for i in range(1, n+1):
    city[i] = list(map(int, input().split()))
    city[i].insert(0, 0)

route = list(map(int, input().split()))
route.insert(0, 0)

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
isConnected = True

for i in range(2, len(route)):
    if index != find(route[i]):
        isConnected = False
        break

if isConnected:
    print("YES")
else:
    print("NO")