# def solution(k, score):
#     answer = []
#     score_in = []
    
#     for i in range(k):
#         score_in.append(score[i])
#         score_in.sort(reverse = True)
#         answer.append(score_in[-1])
    
#     for i in range(k, len(score)):
#         score_in.append(score[i])
#         score_in.sort(reverse = True)
#         del score_in[-1]
#         answer.append(score_in[-1])
    
#     return answer

def solution(k, score):
    answer = []
    score_in = []

    for i in range(len(score)):
        score_in.append(score[i])
        score_in.sort(reverse = True)
        if len(score_in) > k:
            del score_in[-1]
        answer.append(score_in[-1])
    
    return answer