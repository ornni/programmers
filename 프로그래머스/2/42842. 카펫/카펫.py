def solution(brown, yellow):
    answer = []
    range_num = int((brown - 4) / 2)
    for n in range(range_num):
        if n * (range_num - n) == yellow:
            answer.append(n + 2)
            answer.append(range_num - n + 2)
            break
    answer.sort(reverse = True)
    return answer