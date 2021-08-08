n = int(input())  # 컴퓨터의 수
m = int(input())  # 연결된 쌍의 수
matrix = [[0]*(n+1) for i in range(n+1)]
visited_list = [0]*(n+1)

for i in range(m):
    x,y = map(int,input().split())  # 연결되어 있는 번호 쌍
    matrix[x][y] = matrix[y][x] = 1

num = []    # 바이러스 걸리는 컴퓨터 담아줄 리스트

def dfs(V):   # dfs 방법으로 탐색
    visited_list[V] = 1
    for i in range(1,n+1):
        if visited_list[i] == 0 and matrix[V][i] == 1 :
            num.append(1)
            dfs(i)

dfs(1)
print(sum(num))