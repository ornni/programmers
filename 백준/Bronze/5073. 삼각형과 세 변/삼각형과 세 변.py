import sys
input = sys.stdin.readline

lengths = []

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    else:
        lengths.append([a, b, c])

for now_lengths in lengths:
    now_lengths = sorted(now_lengths)
    x = now_lengths[0]
    y = now_lengths[1]
    z = now_lengths[2]

    if z >= (x + y):
        print('Invalid')
    elif x == y and y == z:
        print('Equilateral')
    elif x == y or y == z or z == x:
        print('Isosceles')
    else:
        print('Scalene')