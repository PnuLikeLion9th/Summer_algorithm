n = int(input())#input값
matrix = []
visited = [0 for i in range(n)]
for i in range(n):
    matrix.append(list(map(int,input().split())))

def dfs(start):
    for i in range(n):#연결되어 있고 방문하지 않은 노드라면 방문처리한다.
        if visited[i] == 0 and matrix[start][i] == 1:
            visited[i]=1
            dfs(i)
for i in range(n):#각 행마다 실행
    dfs(i)
    for j in range(n):#dfs가 완료된 시점에 방문처리되어있다면 1을 출력 아니라면 0을 출력
        if visited[j] == 1:
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()#줄바꿈
    visited = [0 for i in range(n)]#다음 노드 연결상태 확인을 위해 방문처리 초기화
    
