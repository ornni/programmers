import sys
input = sys.stdin.readline

n, m = map(int, input().split())
number = list(map(int, input().split()))

sum_list = [0]
cumul = 0

for i in range(n):
    cumul += number[i]
    sum_list.append(cumul)
    
for i in range(m):
    start, end = map(int, input().split())
    print(sum_list[end] - sum_list[start-1])
