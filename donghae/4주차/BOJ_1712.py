A, B, C = map(int,input().split())  #공백기준 입력값 받기
if C-B <= 0:    #손익분기점을 구할 수 없는 경우(가격-생산비 <= 0)
    print(-1)
else:   #이익이 발생하는 지점을 찾기 위해 +1
    print(A//(C-B)+1)
#생산 개수를 n으로 잡고 while문을 만들면 시간초과 발생