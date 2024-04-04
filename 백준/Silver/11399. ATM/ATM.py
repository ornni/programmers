import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

for i in range(n):
    target_data = A[i]
    left_interval = A[i+1:]
    
    for j in range(i):
        if target_data < A[j]:
            interval = A[j:i]
            A = A[:j] + [target_data] + interval + left_interval
            break


cum = []
cum_num = 0
for i in A:
    cum_num += i
    cum.append(cum_num)

print(sum(cum))