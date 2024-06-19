import sys
input = sys.stdin.readline

numbers = [0] * 21
sequence = [0] * 21
visited = [False] * 21
n = int(input())
numbers[0] = 1

for i in range(1, n+1):
    numbers[i] = numbers[i-1] * i

check = list(map(int, input().split()))

if check[0] == 1:
    k = check[1]
    for i in range(1, n+1):
        cnt = 1
        for j in range(1, n+1):
            if visited[j]:
                continue
            if k <= cnt * numbers[n-i]:
                k -= (cnt-1) * numbers[n-i]
                sequence[i] = j
                visited[j] = True
                break
            cnt += 1
    for i in range(1, n+1):
        print(sequence[i], end =' ')
else:
    k = 1
    for i in range(1, n+1):
        cnt = 0
        for j in range(1, check[i]):
            if not visited[j]:
                cnt += 1
        k += cnt * numbers[n-i]
        visited[check[i]] = True
    print(k)