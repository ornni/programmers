def solution(people, limit):
    answer = 0
    
    people.sort()
    index1 = 0
    index2 = len(people) - 1
    
    while index1 <= index2:
        if index1 == index2:
            answer += 1
            break
        if people[index1] + people[index2] <= limit:
            index1 += 1
        index2 -= 1
        answer += 1
    
    return answer
            
    
    
    return answer