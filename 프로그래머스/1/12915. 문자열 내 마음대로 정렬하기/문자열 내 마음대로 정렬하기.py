def solution(strings, n):
    strings_sorted = sorted(strings, key = lambda x : (x[n], x))
    return strings_sorted