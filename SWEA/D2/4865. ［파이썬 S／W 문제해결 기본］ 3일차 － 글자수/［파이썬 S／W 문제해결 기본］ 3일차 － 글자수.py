T = int(input())

for tc in range(T):
    str1= input()
    str2= input()

    count_dict = {}

    for i in str1:
        if i in count_dict.keys():
            continue
        else:
            count_dict[i] = 0

    for j in str2:
        if j in count_dict.keys():
            count_dict[j] += 1
    
    sorted_dict = sorted(count_dict.items(), key = lambda x: x[1], reverse = True)

    print(f'#{tc+1}', sorted_dict[0][1])