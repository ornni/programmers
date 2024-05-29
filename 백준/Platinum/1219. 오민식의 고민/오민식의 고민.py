import sys
input = sys.stdin.readline

n, scity, ecity, m = map(int, input().split())
A = []
distance = [-sys.maxsize] * n

for i in range(m):
    s, e, p = map(int, input().split())
    A.append((s, e, p))

money = list(map(int, input().split()))

distance[scity] = money[scity]

for i in range(n + 101):
    for s, e, p in A:
        if distance[s] == -sys.maxsize:
            continue
        elif distance[s] == sys.maxsize:
            distance[e] = sys.maxsize
        elif distance[e] < distance[s] + money[e] - p:
            distance[e] = distance[s] + money[e] - p
            if i >= n-1:
                distance[e] = sys.maxsize

if distance[ecity] == -sys.maxsize:
    print('gg')
elif distance[ecity] == sys.maxsize:
    print("Gee")
else:
    print(distance[ecity])