def bonus(num, bonus_num):
    if bonus_num == 'S':
        return num ** 1
    elif bonus_num == 'D':
        return num ** 2
    else:
        return num ** 3


def solution(dartResult):
    answer = 0
    answer_list = [0]
    score = []

    for char in dartResult:
        if char.isdigit():
            if score:
                if len(score) == 2:
                    result1 = bonus(int(score[0]), score[1])
                    answer_list.append(result1)
                    score = []

                elif len(score) == 3:
                    result1 = bonus(int(score[0]), score[1])

                    if score[2] == '*':
                        answer_list[-1] *= 2
                        answer_list.append(result1 * 2)
                    elif score[2] == '#':
                        answer_list.append(result1 * (-1))
                    score = []

            if len(score) > 0 and score[-1].isdigit():
                score[-1] = int(score[0])* 10 + int(char)
                score[-1] = str(score[-1])
            else:
                score.append(char)
        else:
            score.append(char)

    if score:
        if len(score) == 2:
            result1 = bonus(int(score[0]), score[1])
            answer_list.append(result1)

        elif len(score) == 3:
            result1 = bonus(int(score[0]), score[1])

            if score[2] == '*':
                answer_list[-1] *= 2
                answer_list.append(result1 * 2)
            elif score[2] == '#':
                answer_list.append(result1 * (-1))
    
    return sum(answer_list)