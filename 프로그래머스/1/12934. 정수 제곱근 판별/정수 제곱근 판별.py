import math

def solution(n):
    answer = 0
    num_sqrt = math.sqrt(n)
    
    if num_sqrt == int(num_sqrt):
        answer = (math.sqrt(n) + 1) ** 2
    else:
        answer = -1
        
    return answer