import sys
from queue import PriorityQueue
print = sys.stdout.write
input = sys.stdin.readline

n = int(input())
queue = PriorityQueue()

for i in range(n):
    request = int(input())
    if request == 0:
        if queue.empty():
            print('0\n')
        else:
            tmp = queue.get()
            print(str((tmp[1])) + '\n')
    else:
        queue.put((abs(request), request))