T = int(input())

for tc in range(T):
    sentence = list(map(str, input().split()))
    stack = []
    answer = 'error'

    for i in sentence:
        if i.isdigit():
            stack.append(int(i))

        elif i == '+':
            if len(stack) >= 2:
                now1 = stack.pop()
                now2 = stack.pop()
                new = now2 + now1
                stack.append(new)
            else:
                break
        elif i == '-':
            if len(stack) >= 2:
                now1 = stack.pop()
                now2 = stack.pop()
                new = now2 - now1
                stack.append(new)
            else:
                break
        elif i == '*':
            if len(stack) >= 2:
                now1 = stack.pop()
                now2 = stack.pop()
                new = now2 * now1
                stack.append(new)
            else:
                break
        elif i == '/':
            if len(stack) >= 2:
                now1 = stack.pop()
                now2 = stack.pop()
                new = now2 // now1
                stack.append(new)
            else:
                break
        elif i == '.':
            if len(stack) == 1:
                answer = stack.pop()
                break
            else:
                break
            
    print(f'#{tc+1}', answer)