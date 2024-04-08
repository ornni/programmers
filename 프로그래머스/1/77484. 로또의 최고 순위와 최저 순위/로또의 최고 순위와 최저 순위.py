def rank(x):
    if x == 6:
        return 1
    elif x == 5:
        return 2
    elif x == 4:
        return 3
    elif x == 3:
        return 4
    elif x == 2:
        return 5
    else:
        return 6
    
def solution(lottos, win_nums):
    count = 0
    answer = []
    
    for i in lottos:
        for j in win_nums:
            if i == j:
                count += 1
    answer.append(rank(count))
    
    for i in lottos:
        if i == 0:
            count += 1
    answer.append(rank(count))
    answer.sort()
    return answer