def solution(numbers, target):
    global answer
    answer = 0
    
    def dfs(index, total):
        global answer
        if index == len(numbers):
            if target == total:
                answer += 1
            return
        dfs(index+1, total + numbers[index])
        dfs(index+1, total - numbers[index])
        return
    
    dfs(0, 0)
    
    return answer