def solution(n, m, section):
    answer = 0
    place = [1] * n
    
    for i in section:
        place[i-1] = 0
    
    for i in section:
        if place[i-1] == 0:
            place[i-1 : i+m-1] = [1] * m
            answer += 1    
    return answer
