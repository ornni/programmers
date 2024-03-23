def solution(k, m, score):
    
    score.sort(reverse = True)
    total_price = 0
    
    for i in range(len(score)//m):
        box = score[m*i : m*(i+1)]
        total_price += box[-1]*m
    return total_price