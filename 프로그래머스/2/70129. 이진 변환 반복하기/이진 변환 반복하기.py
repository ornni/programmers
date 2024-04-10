def solution(s):
    answer = []
    
    zero = 0
    count = 0
    
    while s != '1':
        one_index = []
        for i in range(len(s)):
            if s[i] == '0':
                zero += 1
            else:
                one_index.append(s[i])
                
        no_zero = "".join(one_index)
        len_s = len(no_zero)
        s = bin(len_s)[2:]
        count += 1

    answer.append(count)
    answer.append(zero)
    
    return answer