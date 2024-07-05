import sys
input = sys.stdin.readline

n = int(input())
x_list = []
y_list = []
answer = 0

for _ in range(n):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

x_list.append(x_list[0])
y_list.append(y_list[0])

for i in range(n):
    answer += (x_list[i] * y_list[i+1] - x_list[i+1] * y_list[i])

print(round(abs(answer / 2), 1))