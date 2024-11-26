test_case = int(input())

for tc in range(test_case):

    s = str(input())
    n = len(s)
    
    def palindrome(text):
        for i in range(len(text)//2):
            if text[i] != text[(-1)-i]:
                return False
        return True
    
    cond1 = palindrome(s)
    end_index = int((n-1)/2)
    cond2 = palindrome(s[ : end_index])
    start_index = int(((n-1)/2)*(-1))
    cond3 = palindrome(s[start_index : ])
    
    if cond1 & cond2 & cond3 :
        print(f'#{tc+1} YES')
    else:
        print(f'#{tc+1} NO')