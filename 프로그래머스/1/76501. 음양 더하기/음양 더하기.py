def solution(absolutes, signs):
    
    new_num = []
    for i in range(len(absolutes)):
        if signs[i] == True:
            new_num.append(absolutes[i])
        else:
            new_num.append((-1) * absolutes[i])
    answer = sum(new_num)
    
    return answer