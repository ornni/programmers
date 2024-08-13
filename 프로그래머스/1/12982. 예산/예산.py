def solution(d, budget):
    answer = 0
    left = budget
    
    d.sort()
    
    for i in d:
        if i <= left:
            answer += 1
            left -= i
    
    return answer