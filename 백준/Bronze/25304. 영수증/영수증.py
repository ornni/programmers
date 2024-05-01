import sys
input = sys.stdin.readline

x = int(input())
n = int(input())
shop = []
total = 0

for _ in range(n):
    price, ea = map(int, input().split())
    shop.append((price, ea))

for i in shop:
    total += i[0] * i[1]

if total == x:
    print("Yes")
else:
    print("No")