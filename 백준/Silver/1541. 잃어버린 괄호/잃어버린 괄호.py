import sys
input = sys.stdin.readline

A = list(map(str, input().split('-')))
answer = 0

def total_sums (x):
    total = 0
    sum_numbers = map(int, x.split('+'))
    for i in sum_numbers:
        total += i
    return total

for i in range(len(A)):
    if i == 0:
        answer += total_sums(A[i])
    else:
        answer -= total_sums(A[i])

print(answer)