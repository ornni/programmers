def solution(phone_number):
    hidden_num = '*' * (len(phone_number) - 4)
    last_num = phone_number[-4:]
    return hidden_num + last_num