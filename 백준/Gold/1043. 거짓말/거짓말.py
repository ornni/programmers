import sys
input = sys.stdin.readline

n, m = map(int, input().split())

true = list(map(int, input().split()))
T = true.pop(0)

party = [[] for _ in range(m)]
for i in range(m):
    party[i] = list(map(int, input().split()))
    del party[i][0]

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

answer = 0

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

def checksame(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return True
    else:
        return False

for i in range(m):
    firstperson = party[i][0]
    for j in range(1, len(party[i])):
        union(firstperson, party[i][j])

for i in range(m):
    firstperson = party[i][0]
    talk = True
    for j in range(T):
        if find(firstperson) == find(true[j]):
            talk = False
            break
    if talk:
        answer += 1

print(answer)