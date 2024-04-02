def solution(n):
    
    number = [0, 1]
    for i in range(2, n+1):
        number.append(number[0] + number[1])
        number.pop(0)
        
    return number[-1]%1234567