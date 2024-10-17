def solution(keymap, targets):
    answer = []
    
    key_dict = {}
    
    for words in keymap:
        for i in range(len(words)):
            now = words[i]
            if now in key_dict.keys():
                key_dict[now] = min(i + 1, key_dict[now])
            else:
                key_dict[now] = i+1
    
    for target_words in targets:
        now_answer = 0
        for now_word in target_words:
            if now_word in key_dict.keys():
                now_answer += key_dict[now_word]
            else:
                now_answer = 0
                break
        
        if now_answer != 0:
            answer.append(now_answer)
        else:
            answer.append(-1)
                
    return answer