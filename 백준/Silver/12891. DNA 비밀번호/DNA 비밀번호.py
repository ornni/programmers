import sys
input = sys.stdin.readline

s, p = map(int, input().split())
DNA = list(input())
check_list = [0] * 4
check = 0
answer_list = list(map(int, input().split()))
answer = 0

def plus(x):
    global check_list, check, answer_list
    if x == 'A': 
        check_list[0] += 1
        if check_list[0] == answer_list[0]:
            check += 1
    elif x == 'C':
        check_list[1] += 1
        if check_list[1] == answer_list[1]:
            check += 1
    elif x == 'G':
        check_list[2] += 1
        if check_list[2] == answer_list[2]:
            check += 1
    elif x == 'T':
        check_list[3] += 1
        if check_list[3] == answer_list[3]:
            check += 1

def minus(x):
    global check_list, check, answer_list
    if x == 'A':
        if check_list[0] == answer_list[0]:
            check -= 1
        check_list[0] -= 1
    elif x == 'C':
        if check_list[1] == answer_list[1]:
            check -= 1
        check_list[1] -= 1
    elif x == 'G':
        if check_list[2] == answer_list[2]:
            check -= 1
        check_list[2] -= 1
    elif x == 'T':
        if check_list[3] == answer_list[3]:
            check -= 1
        check_list[3] -= 1
            
for i in range(4):
    if answer_list[i] == 0:
        check += 1

for i in range(p):
    plus(DNA[i])
    
if check == 4:
    answer += 1

for i in range(p, s):
    j = i - p
    plus(DNA[i])
    minus(DNA[j])
    if check == 4:
        answer += 1
        
print(answer)