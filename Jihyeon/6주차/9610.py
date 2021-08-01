N = int(input())
li = [0,0,0,0,0]
for _ in range(N):
    a, b = map(int, input().split(" "))
    if a==0 or b==0:
        li[4]+=1
    elif a>0 and b>0: 
        li[0]+=1
    elif a>0 and b<0: 
        li[3]+=1
    elif a<0 and b<0: 
        li[2]+=1
    elif a<0 and b>0:
        li[1]+=1
for i in range(5):
    if i!=4:
        print("Q{}: {}".format(i+1, li[i]))
    else:
        print("AXIS: {}".format(li[i]))