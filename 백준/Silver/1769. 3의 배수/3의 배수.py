import sys
input = sys.stdin.readline

number = str(input())[:-1]
answer = 0

while len(number) != 1:
    Sum = 0
    answer += 1
    for i in number:
        Sum += int(i)
    number = str(Sum)

print(answer)

if int(number) % 3 == 0:
    print("YES")
else:
    print("NO")