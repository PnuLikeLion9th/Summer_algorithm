T = input()
for i in range(int(T)): #테스트 수 만큼 반복
    H, W, N = map(int, input().split())
    if N%H == 0:    #손님 번호%층 수가 0인 경우와 아닌 경우 구분
        print(H*100+(N//H))
    else:
        print((N%H)*100+(N//H+1))