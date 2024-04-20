def solution(cards1, cards2, goal):
    answer = ""
    index1 = 0
    index2 = 0
    A = []

    for i in goal:
        if i == cards1[index1]:
            A.append(cards1[index1])
            if index1 < (len(cards1) - 1):
                index1 += 1

        elif i == cards2[index2]:
            A.append(cards2[index2])
            if index2 < (len(cards2) - 1):
                index2 += 1
        else:
            break

    if A == goal:
        answer += "Yes"
    else:
        answer += "No"
    return answer