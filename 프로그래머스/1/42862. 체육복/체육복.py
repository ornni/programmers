def solution(n, lost, reserve):
    clothes = [1] * (n+2)
    
    for i in lost[:]:
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)
                
    for i in lost:
        clothes[i] = 0
    
    lost.sort()
    reserve.sort()
    
    while reserve:
        i = reserve.pop(0)
        if clothes[i] == 0:
            clothes[i] = 1
        elif clothes[i-1] == 0:
            clothes[i-1] = 1
        elif clothes[i+1] == 0:
            clothes[i+1] = 1
        
    return sum(clothes) - 2