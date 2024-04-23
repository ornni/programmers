import sys
import math
input = sys.stdin.readline

n = int(input())
# max_num = 1000000
max_num = 1500000


A = list(range(max_num + 1))
A[1] = 0

for i in range(int(math.sqrt(max_num)) + 1):
    if A[i] == 0:
        continue
    else:
        for j in range(i * i, max_num + 1, i):
            A[j] = 0

def Pelindrome(x):
    data = list(str(x))
    index1 = 0
    index2 = len(data) - 1
    
    while (index1 < index2):
        if data[index1] != data[index2]:
            return False
        index1 += 1
        index2 -= 1
        
    return True

N = n

while True:
    if A[N] != 0:
        if Pelindrome(A[N]):
            print(A[N])
            break
    N += 1