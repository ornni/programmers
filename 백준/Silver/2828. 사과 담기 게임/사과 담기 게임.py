import sys
input = sys.stdin.readline

n, m = map(int, input().split())
j = int(input())
apple = []

for _ in range(j):
    apple.append(int(input()))

m_start = 1
m_end = 1 + (m-1)
count = 0

for i in apple:
    if i > m_end:
        diff = i - m_end
        m_end = i
        m_start = m_start + diff
        count += diff
    elif i < m_start:
        diff = m_start - i
        m_start = i
        m_end = m_end - diff
        count += diff

print(count)