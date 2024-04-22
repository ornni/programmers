n = int(input())
A = [[] for _ in range(n)]

for i in range(n):
    s, e = map(int, input().split())
    A[i].append(e)
    A[i].append(s)

A.sort()
end = -1
answer = 0

for i in A:
    if i[1] >= end:
        answer += 1
        end = i[0]

print(answer)