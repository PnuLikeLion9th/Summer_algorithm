def solution(left,right):
    list=[]
    for i in range(left,right+1):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count%2==0:
            list.append(i)
        else:
            list.append(-i)

    return sum(list)