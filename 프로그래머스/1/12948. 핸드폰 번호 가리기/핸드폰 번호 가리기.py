def solution(phone_number):
    hidden_num = '*' * (len(phone_number) - 4)
    print_num = phone_number[-4:]
    
    return hidden_num + print_num