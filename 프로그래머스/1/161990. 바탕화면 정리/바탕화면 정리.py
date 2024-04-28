def solution(wallpaper):
    x = []
    y = []

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                x.append(i)
                y.append(j)
    lux = min(x)
    luy = min(y)
    rdx = max(x)
    rdy = max(y)
    answer = [lux, luy, rdx + 1, rdy + 1]
    
    return answer