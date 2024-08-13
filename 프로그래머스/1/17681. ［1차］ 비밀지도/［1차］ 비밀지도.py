def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        map = ''
        for j in range(n-1, -1, -1):
            if arr1[i] // (2**j) > 0 or arr2[i] // (2**j) > 0:
                map += '#'
                arr1[i] =  arr1[i] % (2**j)
                arr2[i] =  arr2[i] % (2**j)
            else:
                map += ' '
        answer.append(map)
        
    return answer