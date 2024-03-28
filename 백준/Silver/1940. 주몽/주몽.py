import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
number = list(map(int, input().split()))

one = 0
two = n-1
count = 0

sort_number = sorted(number)

while one < two:
    sum = sort_number[one] + sort_number[two]
    if sum == m:
        count += 1
        one += 1
        two -= 1
    elif sum < m:
        one += 1
    else:
        two -= 1

print(count)