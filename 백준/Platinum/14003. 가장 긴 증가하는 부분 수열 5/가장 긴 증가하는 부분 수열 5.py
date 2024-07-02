import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)

index = 0
maxlength = 1
B = [0] * 1000001
D = [0] * 1000001
ans = [0] * 1000001

B[maxlength] = a[1]
D[1] = 1

def binarysearch(l, r, now):
    while l < r:
        mid = (l + r) // 2
        if B[mid] < now:
            l = mid + 1
        else:
            r = mid
    return l

for i in range(2, n+1):
    if B[maxlength] < a[i]:
        maxlength += 1
        B[maxlength] = a[i]
        D[i] = maxlength
    else:
        index = binarysearch(1, maxlength, a[i])
        B[index] = a[i]
        D[i] = index

print(maxlength)
index = maxlength
x = B[maxlength] + 1

for i in range(n, 0, -1):
    if D[i] == index:
        ans[index] = a[i]
        index -= 1

for i in range(1, maxlength+1):
    print(ans[i], end=' ')