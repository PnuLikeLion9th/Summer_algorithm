from collections import deque

def bfs(start, end):
    queue = deque()
    queue.append(start)
    while queue:
        x = queue.popleft()
        if x == end:
            return visited[x]
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= max_input and visited[nx] == 0: 
                visited[nx] = visited[x] + 1    #방문체크
                queue.append(nx)
n, k = map(int, input().split())
max_input = 100000
visited = [0] * (max_input + 1)
print(bfs(n, k))