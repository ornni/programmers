def solution(n):
    number = str(n)
    N = []

    for i in number:
        N.append(int(i))      

    for i in range(len(N), 0, -1):
        for j in range(i-1):
            if N[j] < N[j+1]:
                tmp = N[j]
                N[j] = N[j+1]
                N[j+1] = tmp
    
    return int(''.join(map(str, N)))