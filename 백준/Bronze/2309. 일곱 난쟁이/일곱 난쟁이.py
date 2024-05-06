import sys
input = sys.stdin.readline

heights = []

for _ in range(9):
    heights.append(int(input()))

total_heights = sum(heights)
del_heights = []

for i in range(1, 9):
    for j in range(i):
        if total_heights - heights[i] - heights[j] == 100:
            del_heights.append(i)
            del_heights.append(j)
            break
    if total_heights - heights[i] - heights[j] == 100:
        break
            
del heights[del_heights[0]]
del heights[del_heights[1]]

heights.sort()

for i in heights:
    print(i)     