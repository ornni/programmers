def solution(numbers):
    number_set = set(numbers)
    answer = sum(set(range(0, 10, 1)) - number_set)
    return answer