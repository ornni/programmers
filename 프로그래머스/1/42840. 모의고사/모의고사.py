def solution(answers):    
    
    answer = []

    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    answer_multiple1 = len(answers) // len(student1)
    answer_multiple2 = len(answers) // len(student2)
    answer_multiple3 = len(answers) // len(student3)

    answer_index1 = len(answers) % len(student1)
    answer_index2 = len(answers) % len(student2)
    answer_index3 = len(answers) % len(student3)

    student1_answer = student1 * answer_multiple1 + student1[:answer_index1]
    student2_answer = student2 * answer_multiple2 + student2[:answer_index2]
    student3_answer = student3 * answer_multiple3 + student3[:answer_index3]

    student1_score = 0
    student2_score = 0
    student3_score = 0

    index = 0

    for i in answers:
        if i == student1_answer[index]:
            student1_score += 1
        if i == student2_answer[index]:
            student2_score += 1
        if i == student3_answer[index]:
            student3_score += 1
        index += 1

    Max = max(student1_score, student2_score, student3_score)

    if student1_score == Max:
        answer.append(1)
    if student2_score == Max:
        answer.append(2)
    if student3_score == Max:
        answer.append(3)
        
    return answer