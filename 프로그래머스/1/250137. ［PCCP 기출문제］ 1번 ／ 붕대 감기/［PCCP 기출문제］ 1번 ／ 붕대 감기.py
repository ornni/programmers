def solution(bandage, health, attacks):
    answer = health
    clear = 0
    attack_time = []
    
    for i in range(len(attacks)):
        attack_time.append(attacks[i][0])
    

    for i in range(attack_time[-1]+1):
        if i in attack_time:
            pos = attack_time.index(i)
            power = attacks[pos][1]
            answer = answer - power
            clear = 0  # *****
            if answer <= 0:
                answer = -1
                break
        else:
            if answer < health:
                answer += bandage[1]
                clear += 1
                if clear == bandage[0]:
                    answer += bandage[2]
                    clear = 0
            
            if answer > health:
                answer = health
                    
    return answer