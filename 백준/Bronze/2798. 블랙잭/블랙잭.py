import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
num = 0
diff1 = 0
diff2 = 0
answer = 0

def diff_min (x, y):
    global m
    diff1 = m - x
    diff2 = m - y
    if diff1 < diff2:
        return x
    else:
        return y

for i in range(n):
    if answer == m:
        break
    for j in range(i+1, n):
        if answer == m:
            break
        for k in range(j+1, n):
            num = A[i] + A[j] + A[k]
            if num > m:
                continue
            answer = diff_min(answer, num)
            if answer == m:
                break

print(answer)