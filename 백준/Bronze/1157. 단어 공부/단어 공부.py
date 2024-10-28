word = input()

word = word.upper()
alpha_count = dict()
answer = []

for i in word:
    if i in alpha_count.keys():
        alpha_count[i] += 1
    else:
        alpha_count[i] = 1

max_count = max(alpha_count.values())

for i, j in alpha_count.items():
    if j == max_count:
        answer.append(i)

if len(answer) == 1:
    print(answer[0])
else:
    print('?')