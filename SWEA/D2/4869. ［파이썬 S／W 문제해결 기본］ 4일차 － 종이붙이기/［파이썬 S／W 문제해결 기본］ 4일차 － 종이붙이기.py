T = int(input())

def func(x):
    global S
    if n >= 3 and len(S) <= x:
        S.append(func(x-1) + 2*func(x-2))
    return S[x]

for tc in range(T):
    N = int(input())

    S = [0, 1, 3]
    n = N // 10

    print(f'#{tc+1}', func(n))