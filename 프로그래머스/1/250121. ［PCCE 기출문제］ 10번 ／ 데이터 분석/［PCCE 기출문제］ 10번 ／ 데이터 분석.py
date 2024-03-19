def solution(data, ext, val_ext, sort_by):

    type = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    
    filtered_data = [x for x in data if x[type[ext]] < val_ext]
    answer = sorted(filtered_data, key = lambda x : x[type[sort_by]])
    
    return answer