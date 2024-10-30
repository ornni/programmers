question_num = int(input())

for i in range(1, question_num + 1):
    x1, y1, x2, y2 = map(int, input().split())

    check = int(input())

    inside_answer = 0
    online_answer = 0
    outside_answer = 0

    for _ in range(check):
        x, y = map(int, input().split())

        if (x1 < x < x2) and (y1 < y < y2):
            inside_answer += 1
        elif ((x == x1 or x == x2) and (y1 <= y <= y2)) or ((x1 <= x <= x2) and (y == y1 or y == y2)):
            online_answer += 1
        else:
            outside_answer += 1
    
    print(f'#{i} {inside_answer} {online_answer} {outside_answer}')