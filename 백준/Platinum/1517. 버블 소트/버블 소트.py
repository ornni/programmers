import sys
input = sys.stdin.readline

result = 0

def merge_sort(s, e):
    global result
    if e - s < 1:
        return
    m = int(s + (e - s) / 2)
    merge_sort(s, m)
    merge_sort(m + 1, e)
    
    
    for i in range(s, e + 1):
        tmp[i] = a[i]
    
    k = s
    index1 = s
    index2 = m + 1

    while index1 <= m and index2 <= e:
        if tmp[index1] > tmp[index2]:
            a[k] = tmp[index2]
            result = result + index2 - k
            k += 1
            index2 += 1
        else:
            a[k] = tmp[index1]
            k += 1
            index1 += 1

    while index1 <= m:
        a[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= e:
        a[k] = tmp[index2]
        k += 1
        index2 += 1
    
n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)
tmp = [0] * int(n + 1)

merge_sort(1, n)

print(result)