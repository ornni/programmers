def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
        elif 'a' <= i <= 'z': 
            new_char = chr((ord(i) - ord('a') + n) % 26 + ord('a'))
            answer += new_char
        elif 'A' <= i <= 'Z': 
            new_char = chr((ord(i) - ord('A') + n) % 26 + ord('A'))
            answer += new_char
    return answer