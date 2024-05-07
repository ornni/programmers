import math

def solution(nums):
    answer = 0
    A = []

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                A.append(nums[i] + nums[j] + nums[k])

    A.sort()
    limit = sum(A[-3:]) + 1

    prime = list(range(limit))
    prime[1] = 0

    for i in range(2, int(math.sqrt(limit))+1):
        for j in range(i*i, limit, i):
            prime[j] = 0

    for i in A:
        if prime[i] != 0:
            answer += 1
    
    return answer