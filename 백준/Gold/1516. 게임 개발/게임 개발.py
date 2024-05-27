from collections import deque

n = int(input())
A = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
answer = [0] * (n+1)

for i in range(1, n+1):
    input_list = list(map(int, input().split()))
    answer[i] = (input_list[0])
    index =1

    while True:
        preTemp = input_list[index]
        index += 1
        if preTemp == -1:
            break
        A[preTemp].append(i)
        indegree[i] += 1

queue = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)

result = [0] * (n+1)

while queue:
    now = queue.popleft()
    for next in A[now]:
        indegree[next] -= 1
        result[next] = max(result[next], result[now] + answer[now])
        if indegree[next] == 0:
            queue.append(next)

for i in range(1, n+1):
    print(result[i] + answer[i])