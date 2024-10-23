def solution(survey, choices):
    answer = ''
    
    result = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    result_keys = list(result.keys())
    
    for i in range(len(survey)):
        score = choices[i] - 4
        
        if score < 0:
            result[survey[i][0]] += abs(score)
        else:
            result[survey[i][1]] += abs(score)
    
    for i in range(4):
        if result[result_keys[2*i]] >= result[result_keys[2*i+1]]:
            answer += result_keys[2*i]
        else:
            answer += result_keys[2*i+1]
            
    return answer