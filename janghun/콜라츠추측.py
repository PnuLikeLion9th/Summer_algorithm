def solution(num):
    time=0
    while num!=1:
        time+=1
        if time==500:
            return(-1)
        elif num%2==0:
            num=num/2
        elif num%2==1:
            num=(num*3)+1
    return time