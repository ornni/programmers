def solution(s):
    count_p = 0
    count_y = 0
    
    s = s.lower()
    
    for i in s:
        if i == 'p':
            count_p += 1
        elif i == 'y':
            count_y += 1

    if count_p == count_y:
        return True
    else:
        return False