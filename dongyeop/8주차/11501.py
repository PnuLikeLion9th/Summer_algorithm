t = int(input())

for _ in range(t):
    answer=0
    max = 0
    d = int(input())
    stock = list(map(int,input().split()))
    for i in range(len(stock)-1,-1,-1):
        if(stock[i])>max:
            max = stock[i]
        else:
            answer+=max-stock[i]
    print(answer)



#뒤에서부터 본다.
#현재 시점이 최고점이 아니라면 이후에 최고점이 나온다는 의미이므로
#지금 다판다.
#그 값이 최대치인지 확인
#최대치라면 판다

