from collections import deque

n, k = map(int,input().split())
queue = deque([])

for i in range(1,n+1):   # 1부터 n까지 배열
    queue.append(i)

print('<',end='')
while queue:             # n명이 모두 제거될 때까지
    for i in range(k-1):  # 순서대로 k번째 사람 제거
        queue.append(queue.popleft())
        
    if len(queue) == 1:
        print(queue.popleft(), end='')  # 마지막 출력시에는 , 없이
    else:
        print(queue.popleft(), end=', ')

print('>')