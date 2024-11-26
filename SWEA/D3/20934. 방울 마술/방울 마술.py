test_case = int(input())

for i in range(test_case):

    cups, k = input().split(' ')
    k = int(k)

    for j in range(3):
        if cups[j] == 'o':
            now = j
            break

    for _ in range(k):
        if now == 0:
            now += 1
        else:
            now -= 1
        
    print(f'#{i+1} {now}')