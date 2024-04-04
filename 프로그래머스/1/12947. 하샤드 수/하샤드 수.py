def solution(x):
    str_x = str(x)
    sum_num = 0
    for i in str_x:
        num = int(i)
        sum_num += num
    if x % sum_num == 0:
        answer = True
    else:
        answer = False
    return answer