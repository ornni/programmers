import sys
input = sys.stdin.readline

birthday = list(map(int, input().split()))
today = list(map(int, input().split()))
a = 0
b = 0
c = 0

c = today[0] - birthday[0]
b = c + 1
a = c - 1

if today[1] > birthday[1]:
    a += 1
elif today[1] == birthday[1]:
    if today[2] >= birthday[2]:
        a += 1

answer = [a, b, c]

for i in answer:
    print(i)