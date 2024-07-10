import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

sum_list = [0]
tmp = 0

for i in a:
    tmp += i
    sum_list.append(tmp)

for i in range(m):
    s, e = map(int, input().split())
    print(sum_list[e] - sum_list[s-1])