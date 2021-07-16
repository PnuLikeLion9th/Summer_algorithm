n= int(input())

matrix = []
for i in range(n):
    matrix.append(list(map(int,input())))

count = []
def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if matrix[x][y] == 1:
        count.append((x,y))
        matrix[x][y] = 0
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False
result = 0
countlist = []
for i in range(n):
    for j in range(n):
        if dfs(i,j)==True:
            result +=1
            countlist.append(len(count))
            count = []
countlist.sort()
print(result)
for i in countlist:
    print(i)