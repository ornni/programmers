def before_month_to_day(x):
    if x <= 2:
        days = 31*(x//2)
        return days 
        
    elif x > 8:
        if x % 2 == 0:
            days = 31*(x//2) + 30*(x//2 - 1)
        else:
            days = 31*(x//2 + 1) + 30*(x//2 - 1)
        return days - 1
        
    else:
        if x % 2 == 0:
            days = 31*(x//2) + 30*(x//2 - 1)
        else:
            days = 31*(x//2) + 30*(x//2)
        return days - 1
    

def weekday(x):
    if x % 7 == 0:
        return 'THU'
    elif x % 7 == 1:
        return 'FRI'
    elif x % 7 == 2:
        return 'SAT'
    elif x % 7 == 3:
        return 'SUN'
    elif x % 7 == 4:
        return 'MON'
    elif x % 7 == 5:
        return 'TUE'
    else:
        return 'WED'
    
def solution(a, b):
    total_day = before_month_to_day(a) + b
    answer = weekday(total_day)
    return answer