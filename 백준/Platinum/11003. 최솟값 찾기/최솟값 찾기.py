from collections import deque

n , l = map(int, input().split())
deq = deque()
A = list(map(int, input().split()))

for i in range(n):
    while deq and deq[-1][0] > A[i]:
        deq.pop()
    deq.append((A[i], i))
    
    if deq[0][1] <= i-l:
        deq.popleft()
    
    print(deq[0][0], end = ' ')