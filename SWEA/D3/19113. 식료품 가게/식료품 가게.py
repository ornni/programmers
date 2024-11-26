test_case = int(input())

for tc in range(test_case):

    n = int(input())
    p = list(map(int, input().split()))
    

    discount_price = []

    while p:
        price = p[-1] * 0.75
        price_index = p.index(price)
        del p[-1]
        del p[price_index]

        discount_price.append(int(price))
        
    discount_price.sort()

    print(f'#{tc+1} {" ".join(map(str, discount_price))}')