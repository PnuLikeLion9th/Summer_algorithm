n = int(input())
load = list(map(int,input().split()))
gas = list(map(int,input().split()))
charge = gas[0]
length = 0
answer = 0
#그러니까 현재 마을 보다 낮은 기름값이 나올때까지의 로드만큼 기름을 넣으면 됨
for i in range(1,len(gas)):
    answer+=charge*load[i-1]
    if gas[i]<charge:
        charge = gas[i]

print(answer)
    


    
        
