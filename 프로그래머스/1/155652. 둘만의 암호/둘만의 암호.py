def solution(s, skip, index):
    answer = ''
    s = list(s)

    for _ in range(len(s)):
        check = 0
        move = 1
        while check != index:
            alpha = chr((ord(s[0]) + move - ord('a')) % 26 + ord('a'))
            if alpha not in skip:
                check += 1
                move += 1
            else:
                move += 1
        s.pop(0)
        answer += alpha

    return answer