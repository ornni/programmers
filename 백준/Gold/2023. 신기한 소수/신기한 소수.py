import sys
input = sys.stdin.readline

n = int(input())

def prime(x):
    for i in range(2, int((x/2)+1)):
        if x % i == 0:
            return False
    return True

def DFS(num):
    if len(str(num)) == n:
        print(num)
    else:
        for i in range(1, 10):
            if i % 2 == 0:
                continue
            if prime(num * 10 + i):
                DFS(num * 10 + i)
DFS(2)
DFS(3)
DFS(5)
DFS(7) 