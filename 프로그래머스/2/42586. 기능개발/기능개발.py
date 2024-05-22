def solution(progresses, speeds):
    answer = []
    days = [0] * len(progresses)
    count = 0

    for i in range(len(progresses)):
        progresses[i] = 100 - progresses[i]

    for i in range(len(progresses)):
        if (progresses[i] % speeds[i]) != 0:
            days[i] = (progresses[i] // speeds[i]) + 1
        else:
            days[i] = (progresses[i] // speeds[i])

    Max = days[0]

    for i in days:
        if i <= Max:
            count += 1
        else:
            answer.append(count)
            count = 1
            Max = max(Max, i)

    answer.append(count)
    
    return answer