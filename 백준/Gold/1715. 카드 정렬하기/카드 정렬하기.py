import sys
input = sys.stdin.readline
from queue import PriorityQueue

n = int(input())
queue = PriorityQueue()

for i in range(n):
    queue.put(int(input()))

a = 0
b = 0
sum = 0

while queue.qsize() > 1:
    a = queue.get()
    b = queue.get()
    new = a + b
    queue.put(new)
    sum += new

print(sum)