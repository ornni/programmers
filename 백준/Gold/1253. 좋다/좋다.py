import sys
input = sys.stdin.readline

n = int(input())
number = list(map(int, input().split()))
answer = 0
sort_number = sorted(number)

for k in range(n):
    target = sort_number[k]
    one = 0
    two = n-1
    while one < two:
        sum = sort_number[one] + sort_number[two]
        if sum == target:
            if one != k and two != k:
                answer += 1
                break
            elif one == k:
                one += 1
            elif two == k:
                two -= 1
        elif sum < target:
            one += 1
        else:
            two -= 1

print(answer)