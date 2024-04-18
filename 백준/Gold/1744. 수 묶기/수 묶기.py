import sys
input = sys.stdin.readline
from queue import PriorityQueue

n = int(input())
plus_queue = PriorityQueue()
minus_queue = PriorityQueue()
one = 0
zero = 0
a = 0
b= 0
sum = 0

for i in range(n):
    data = int(input())
    if data > 1:
        plus_queue.put(data * (-1))
    elif data == 1:
        one += 1
    elif data == 0:
        zero += 1
    else:
        minus_queue.put(data)
        

while plus_queue.qsize() > 1:
    a = plus_queue.get() * (-1)
    b = plus_queue.get() * (-1)
    sum += a * b

if plus_queue.qsize() > 0:
    sum += plus_queue.get() * (-1)

while minus_queue.qsize() > 1:
    a = minus_queue.get()
    b = minus_queue.get()
    sum += a * b

if minus_queue.qsize() > 0:
    if zero == 0:
        sum += minus_queue.get()

sum += one
print(sum)