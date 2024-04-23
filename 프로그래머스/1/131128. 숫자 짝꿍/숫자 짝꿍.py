def solution(X, Y):
    answer = []

    for i in range(9, -1, -1):
        x = X.count(str(i))
        y = Y.count(str(i))
        
        if min(x, y) > 0:
            for j in range(min(x, y)):
                answer.append(i)

    if answer:
        if any(answer) == False:
            return "0"
        else:
            return ''.join(map(str, answer))
    else:
        return "-1"