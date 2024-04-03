import sys
input = sys.stdin.readline
print = sys.stdout.write
from queue import PriorityQueue

n = int(input())
queue = PriorityQueue()

for i in range(n):
    request = int(input())
    
    if request == 0:
        if queue.empty():
            print('0\n')
        else:
            temp = queue.get()
            print(str((temp[1])) + '\n')
    else:
        queue.put((abs(request), request))