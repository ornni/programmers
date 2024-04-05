def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        answer_element = []
        for j in range(len(arr2[1])):
            element = 0
            for k in range(len(arr1[1])):
                element += arr1[i][k] * arr2[k][j]
            answer_element.append(element)
        answer.append(answer_element)
    
    return answer