import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A.reverse()


answer = [A[0], 1]

for i in A[1:]:
    tmp = answer[0]
    answer[0] = answer[1]
    answer[1] = tmp
    
    answer[0] = (answer[1] * i) + answer[0]

tmp = answer[0]
answer[0] = answer[1]
answer[1] = tmp

answer[0] = answer[1] - answer[0]

print(*answer)