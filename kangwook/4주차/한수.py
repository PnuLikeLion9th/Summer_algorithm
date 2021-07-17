x= int(input())
if x<100:   #범위를 4가지로 나눈다.
    count=x
elif 100<=x and x<=110:
    count=99
elif x>110 and x<1000:
    count=99
    for i in range(111,x+1):    #for문을 이용하여 범위에 있는 모든 수에 대해 등차 검사
        t=str(i)
        if int(t[0])-int(t[1]) == int(t[1])-int(t[2]):  #등차수열의 성질 이용
            count+=1
elif x==1000:
    count=144
print(count)