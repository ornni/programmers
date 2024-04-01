def solution(s):
    
    answer = sorted(s, key = lambda x: (x, x.lower()), reverse = True)
    
    
    return ''.join(answer)