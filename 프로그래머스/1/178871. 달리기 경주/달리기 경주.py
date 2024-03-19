# def solution(players, callings):
#     index = 0

#     for i in range(len(callings)):
#         index = players.index(callings[i])
#         players[index -1], players[index] = players[index], players[index-1]
#     return players

# 용량이 너무 커서 시간초과가 나옴

def solution(players, callings):
    rank = {idx: player for player, idx in enumerate(players)}
    for called in callings:
        idx = rank.get(called)
        go_back_player = players[idx-1]
        
        rank[called] = idx-1
        rank[go_back_player] = idx

        players[idx-1] = called
        players[idx] = go_back_player
        
    return players