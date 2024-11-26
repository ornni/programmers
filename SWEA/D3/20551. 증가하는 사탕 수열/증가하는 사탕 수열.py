test_case = int(input())

for t in range(test_case):

    box_list = list(map(int, input().split()))
    eat = 0

    for i in range(2, 0, -1):

        if box_list[i-1] >= box_list[i]:
            limit = box_list[i] - 1
            eat += (box_list[i-1] - limit)
            box_list[i-1] = limit

        if 0 in box_list:
                eat = -1
                break
        
    print(f'#{t+1} {eat}')