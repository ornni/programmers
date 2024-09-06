def has_repeating_digits(number):
    num_str = str(number)
    return len(num_str) != len(set(num_str))

while True:
    try:
        n, m = map(int, input().split())
        
        count = 0
        for i in range(n, m+1):
            if not has_repeating_digits(i):
                count += 1
        
        print(count)
    
    except EOFError:
        break