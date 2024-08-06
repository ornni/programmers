def solution(babbling):
    count = 0
    can_speak = ['aya', 'ye', 'woo', 'ma']
    cant_speak = ['ayaaya', 'yeye', 'woowoo', 'mama']
    
    for i in range(len(babbling)):
        word = babbling[i]
        
        for k in cant_speak:
            if k in word:
                word = word.replace(k, 'x')

        for j in can_speak:
            if j in word:
                word = word.replace(j, ' ')
                
        word = word.replace(' ', '')
        if not word:
            count += 1
    
    return count