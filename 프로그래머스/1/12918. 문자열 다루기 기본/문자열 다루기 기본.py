def solution(s):
    answer = False
    
    if len(s) == 4 or len(s) == 6:
        answer = True
        for i in s:
            if not i.isdigit():
                answer = False
                break
            
    return answer