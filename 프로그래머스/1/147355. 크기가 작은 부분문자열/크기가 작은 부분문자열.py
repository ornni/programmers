def solution(t, p):
    answer = 0
    number = []

    for i in range(len(t) - len(p) + 1):
        number.append(t[i : i + len(p)])
        
    for i in number:
        if int(i) <= int(p):
            answer += 1
    
    return answer