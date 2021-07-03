T = int(input())
for _ in range(T):
    N=int(input())
    max=0
    mname=""
    for _ in rangw(N):
        name,num=input().split()
        num=int(num)
        if(num>max):
            max=num
            mname=name
    print(mname)