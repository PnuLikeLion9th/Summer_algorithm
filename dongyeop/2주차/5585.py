n = int(input())
re = 1000-n#거스름돈
answer=0
while re>0:#0원이 될때까지 반복 가장 큰돈부터 거슬러 준다.
    if re>=500:
        re-=500
        answer+=1
    elif re>=100:
        re-=100
        answer+=1
    elif re>=50:
        re-=50
        answer+=1
    elif re>=10:
        re-=10
        answer+=1
    elif re>=5:
        re-=5
        answer+=1
    else:
        re-=1
        answer+=1
print(answer)
