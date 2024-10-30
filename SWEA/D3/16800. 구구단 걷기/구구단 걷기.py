question_num = int(input())

for i in range(1, question_num + 1):
    n = int(input())

    multi = 1

    for j in range(1, int(n**0.5) + 1):
        if n % j == 0:
            multi = max(multi, j)
        
    answer1 = multi - 1
    answer2 = (n // multi) - 1

    print(f"#{i} {answer1 + answer2}")