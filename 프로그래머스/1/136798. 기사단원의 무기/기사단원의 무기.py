def solution(number, limit, power):
    
    divisor = []
    count = 0
    
    for i in range(1, number+1):
        count = 0
        interval = int((i)**0.5)
        for j in range(1, interval+1):
            if i%j == 0:        
                if i == j**2:
                    count += 1
                else:
                    count += 2
        divisor.append(count)

    for i in range(number):
        if divisor[i] > limit:
            divisor[i] = power
    
    return sum(divisor)