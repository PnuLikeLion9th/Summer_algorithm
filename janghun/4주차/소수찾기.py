from math import sqrt
def solution(n):
    answer = 0
    for i in range(2,n+1):
        ans=True
        for prime in range(2,int(sqrt(i))+1):
            if i%prime == 0:
                ans=False
                
                break
        if ans==True:
            answer+=1
            
    return answer