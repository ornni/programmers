import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
start = 1
end = k
answer = 0

while start <= end:
    median = int((start + end) / 2)
    cnt = 0
    
    for i in range(1, n+1):
        cnt += min(int(median / i), n)
    if cnt < k:
        start = median + 1
    else:
        answer = median
        end = median - 1

print(answer)