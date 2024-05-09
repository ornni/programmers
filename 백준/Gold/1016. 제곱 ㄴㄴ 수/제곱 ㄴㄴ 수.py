import sys
import math

Min, Max = map(int, input().split())
check = [False] * (Max - Min + 1)

for i in range(2, int(math.sqrt(Max) + 1)):
    divisor = i * i
    start = int(Min/divisor)
    if Min % divisor != 0:
        start += 1
    for j in range(start, int(Max/divisor) + 1):
        check[int(j * divisor) - Min] = True

answer = 0

for i in range(Max - Min + 1):
    if not check[i]:
        answer += 1

print(answer)