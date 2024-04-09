def solution(ingredient):
    answer = 0
    hamburger = [1, 2, 3, 1]
    in_the_burger = []
    i = 0
         
    for i in ingredient:
        in_the_burger.append(i)
        if len(in_the_burger) < 4:
            continue
        else:
            if in_the_burger[-4:] == hamburger:
                answer += 1
                del in_the_burger[-4:]
            
    return answer
