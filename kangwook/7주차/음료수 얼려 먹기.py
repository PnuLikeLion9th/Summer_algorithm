#connected component 찾기
n,m = map(int,input().split()) #가로 m 세로 n
graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))

count=0

def dfs(x,y):
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True

    return False

for i in range(n):
    for j in range(m):
        if dfs(j,i) == True:
            count+=1

print(count)
