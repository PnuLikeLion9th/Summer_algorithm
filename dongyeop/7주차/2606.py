#Dfs로
# n = int(input())
# m = int(input())

# matrix = [[0]*(n+1)]*(n+1)
# visitied = [False]*(n+1)
# for _ in range(m):
#     a,b = map(int,input().split())
#     matrix[a][b] = matrix[b][a]=1

# result = []
# def dfs(v):
#     visitied[v] = True#시작노드 방문체크
#     for i in range(1,n+1):
#         if matrix[v][i] == 1 and visitied[i] == False:
#             result.append(i)
#             dfs(i)

#     return len(result)
# print(dfs(1))

n = int(input())
m = int(input())
matrix = [[0]*(n+1) for i in range(n+1)]
visited = [0]*(n+1)
#matrix = [[0]*(n+1)]*(n+1) for 문과 다르다. 


for _ in range(m):
    a,b = map(int,input().split())
    matrix[a][b] = matrix[b][a] =1
result = []
def dsf(v):
    visited[v]= 1

    for i in range(1,n+1):
        if matrix[v][i] == 1 and visited[i] == 0:
            result.append(i)
            dsf(i)
    return len(result)

print(dsf(1))