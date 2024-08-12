def solution(N, stages):
    answer = []
    count = [[0, i] for i in range(0, N+2)]
    
    for i in stages:
        count[i][0] += 1
    
    if count[N+1][0] != 0:
        Sum = count[N+1][0]
    else:
        Sum = 0.00000000000001
    
    for i in range(N, -1, -1):
        Sum += count[i][0]
        count[i][0] = count[i][0] / Sum
    
    del count[0]
    del count[-1]
    
    count = sorted(count, key = lambda x:(-x[0], x[1]))
    
    for i in count:
        answer.append(i[1])
        
    return answer