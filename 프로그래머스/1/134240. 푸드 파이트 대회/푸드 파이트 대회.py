def solution(food):
    answer = ''
    count = 0
    for i in range(1, len(food)):
        count = food[i] // 2
        answer = answer + f'{i}'*count
    reverse = answer[::-1]
    answer = answer + '0' + reverse
    return answer