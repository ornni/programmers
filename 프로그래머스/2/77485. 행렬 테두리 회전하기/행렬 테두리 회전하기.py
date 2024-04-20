def move(data, x1, y1, x2, y2):
    left = data[x1][y2]
    right = data[x2][y1]
    min_num = min(left, right)

    for i in range(y2, y1, -1):
        data[x1][i] = data[x1][i-1]
        min_num = min(min_num, data[x1][i-1])

    for i in range(y1, y2):
        data[x2][i] = data[x2][i+1]
        min_num = min(min_num, data[x2][i+1])
        
    for i in range(x2, x1, -1):
        data[i][y2] = data[i-1][y2]
        min_num = min(min_num, data[i-1][y2])

    for i in range(x1, x2):
        data[i][y1] = data[i+1][y1]
        min_num = min(min_num, data[i+1][y1])

    data[x2-1][y1] = right
    data[x1+1][y2] = left
    
    return data, min_num

def solution(rows, columns, queries):
    answers = []
    number = 1
    numbers = [[0] * (columns + 1)]
    for _ in range(rows):
        row_add = [0]
        for _ in range(columns):
            row_add.append(number)
            number += 1
        numbers.append(row_add)
    
    for i in queries:
        numbers, answer = move(numbers, i[0], i[1], i[2], i[3])
        answers.append(answer)
    
    return answers