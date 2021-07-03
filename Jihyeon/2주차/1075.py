N = input()                       # 문자열 조작을 위해 int형으로 변환x
F = int(input())

N = int(N[:-2] + "00")            # N에서 뒤에서 두 개 숫자를 00으로 바꾸고 int형으로 변환해 저장
 
for i in range(100):
    if (N + i) % F == 0:          # N과 현재 숫자의 합이 F로 나누어 떨어지고
        if 0 <= i <= 9:           # 현재 숫자가 한 자리 숫지면
            print("0" + str(i))   # 앞에 0을 붙여 두 자리로 출력
            break
        else :
            print(i)              # 현재 숫자가 두 자리면 그대로 출력
        break