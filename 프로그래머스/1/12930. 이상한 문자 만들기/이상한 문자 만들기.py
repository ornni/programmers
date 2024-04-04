def solution(s):

    result = []
    word = s.split(" ")
    for i in range(len(word)):
        answer = ''
        for j, char in enumerate(word[i]):
            if j % 2 == 0:
                answer += char.upper()
            else:
                answer += char.lower()
        result.append(answer)
        
    return ' '.join(result)