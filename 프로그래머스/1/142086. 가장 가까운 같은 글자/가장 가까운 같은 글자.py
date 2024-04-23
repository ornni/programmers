def solution(s):
    answer = []
    index = -1
    for i in range(len(s)):
        indexs= []
        for j in range(i-1, -1, -1):
            if s[i] == s[j]:
                index = i - j
                indexs.append(index)
        if indexs:
            answer.append(min(indexs))
        else:
            answer.append(-1)
            
    return answer