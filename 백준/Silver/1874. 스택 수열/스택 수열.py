import sys
input = sys.stdin.readline

n = int(input())
seq = []

for i in range(n):
    seq.append(int(input()))
    
start = 1
stack = []
result = True
answer = ''

for i in range(n):
    if seq[i] >= start:
        while seq[i] >= start:
            stack.append(start)
            start += 1
            answer += '+\n'
        stack.pop()
        answer += '-\n'
    else:
        num = stack.pop()
        if num > seq[i]:
            print('NO')
            result = False
            break
        else:
            answer += '-\n'

if result:
    print(answer)