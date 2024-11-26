test_case = int(input())

for test in range(test_case):

    n, m = map(int, input().split())
    s = list(map(str, input().split()))
    t = list(map(str, input().split()))
    q = int(input())

    questions = []
    for _ in range(q):
        question = int(input())
        questions.append(question)
    
    answer = ''
    str_list = []
    S = s * m
    T = t * n

    for i in range(n * m):
        word = S[i] + T[i]
        str_list.append(word)
    
    for j in questions:
        left = j % (n * m)

        if left == 0:
            answer += str_list[-1]
        else:
            answer += str_list[left - 1]
        
        answer += ' '
        
    print(f'#{test+1} {answer}')