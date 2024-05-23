def solution(s):
    answer = True
    check = 0
    
    for i in s:
        if i == "(":
            check += 1
        elif i == ")":
            check -= 1
        
        if check < 0:
            answer = False
            break
    
    if not answer:    
        return False
    elif check == 0:
        return True
    else:
        return False