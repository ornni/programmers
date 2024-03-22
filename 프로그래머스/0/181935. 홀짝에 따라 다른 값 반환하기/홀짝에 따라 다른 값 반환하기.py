def solution(n):
    answer = 0
    if n%2 == 1:
        answer = sum(range(1, n+1, 2))
    else:
        even = range(2, n+1, 2)
        even = [x**2 for x in even]
        answer = sum(even)
    return answer