def solution(s):
    if len(s) % 2 == 0:
        start = len(s) // 2
        return (s[start - 1 : start + 1])
    else:
        return (s[len(s) // 2])