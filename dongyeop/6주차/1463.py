#dynamic programming
#상향식 방식
x = int(input())

d = [0]*1000001

for i in range(2,x+1):
    d[i] = d[i-1]+1
    if i%2 == 0:
        d[i] = min(d[i],d[i//2]+1)
    if i%3 == 0:
        d[i] = min(d[i],d[i//3]+1)

print(d[x])
#dp문제는 점화식을 찾아내는것이 핵심이닷!!