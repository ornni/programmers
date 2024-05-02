import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())

def isPrime(x):
    for i in range(2, int(x/2)+1):
        if x % i == 0:
            return False
    return True

def DFS(x):
    if len(str(x)) == n:
        print(x)
    else:
        for i in range(1, 10, 2):
            if isPrime(x * 10 + i):
                DFS(x * 10 + i)

DFS(2)
DFS(3)
DFS(5)
DFS(7)