import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque([])

for i in range(n):
    a = sys.stdin.readline().split()

    if a[0] == 'push':
        queue.append(a[1])
    elif a[0] == 'pop':  
        if not queue:
            print(-1)
        else:
            print(queue.popleft())  # del 함수를 사용하게 되면 시간 초과(지우고 값들을 옮겨주는 과정이 필요하므로)
    elif a[0] == 'size':
         print(len(queue))
    elif a[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif a[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])