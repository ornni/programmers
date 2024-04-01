import sys
input = sys.stdin.readline

need_list = [0]*4
now_list = [0]*4
check = 0

def add_in_list(x):
    global need_list, now_list, check
    
    if x == 'A':
        now_list[0] += 1
        if now_list[0] == need_list[0]:
            check += 1
    
    elif x == 'C':
        now_list[1] += 1
        if now_list[1] == need_list[1]:
            check += 1
    
    elif x == 'G':
        now_list[2] += 1
        if now_list[2] == need_list[2]:
            check += 1
    
    else:
        now_list[3] += 1
        if now_list[3] == need_list[3]:
            check += 1

def remove_in_list(x):
    global need_list, now_list, check
    
    if x == 'A':
        if now_list[0] == need_list[0]:
            check -= 1
        now_list[0] -= 1
    
    elif x == 'C':
        if now_list[1] == need_list[1]:
            check -= 1
        now_list[1] -= 1
        
    elif x == 'G':
        if now_list[2] == need_list[2]:
            check -= 1
        now_list[2] -= 1
    
    else:
        if now_list[3] == need_list[3]:
            check -= 1
        now_list[3] -= 1

s, p = map(int, input().split())
A = list(input())
result = 0
need_list = list(map(int, input().split()))

for i in range(4):
    if need_list[i] == 0:
        check += 1

for i in range(p):
    add_in_list(A[i])
    
if check == 4:
    result += 1

for i in range(p, s):
    j = i - p
    add_in_list(A[i])
    remove_in_list(A[j])
    
    if check == 4:
        result += 1

print(result)
    