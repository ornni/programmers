import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
A = [False] * (m - n + 1)

for i in range(2, int(math.sqrt(m) + 1)):
    divisor = i * i
    index = int(n / divisor)
    if n % divisor != 0:
        index += 1
    for j in range(index, int(m / divisor) + 1):
        A[int((j * divisor) - n)] = True
    
answer = 0

for i in range(m - n + 1):
    if not A[i]:
        answer += 1

print(answer)