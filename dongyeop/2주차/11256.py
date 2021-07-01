n = int(input())
for _ in range(n):
    j,boxn = map(int,input().split())
    boxsize = []
    answer = 0
    for _ in range(boxn):
        x,y= map(int,input().split())
        boxsize.append(x*y)
    boxsize.sort(reverse=True)
    for i in boxsize:
        if j>0:
            j-=i
            answer+=1
        else:
            print(answer)
            break
