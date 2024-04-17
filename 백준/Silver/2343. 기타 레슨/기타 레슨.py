import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
start = 0
end = 0

for i in A:
    if start < i:
        start = i
    end += i
    
while start <= end:
    median = int((start + end) / 2)
    sum = 0
    count = 0
    for i in range(n):
        if sum + A[i] > median:
            count += 1
            sum = 0
        sum += A[i]
    if sum != 0:
        count += 1
    if count > m:
        start = median + 1
    else:
        end = median - 1

print(start)