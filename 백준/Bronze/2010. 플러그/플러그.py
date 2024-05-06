import sys
input = sys.stdin.readline

n = int(input()) 
plug = []

for _ in range(n):
    plug.append(int(input()))

print(sum(plug) - n + 1)