import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

answer = 0
A.sort()

for i in range(n):
    find = A[i]
    index1 = 0
    index2 = n - 1
    while index1 < index2:
        total = A[index1] + A[index2]
        if total == find:
            if index1 != i and index2 != i:
                answer += 1
                break
            elif index1 == i:
                index1 += 1
            elif index2 == i:
                index2 -= 1
        elif total < find:
            index1 += 1
        else:
            index2 -= 1

print(answer)