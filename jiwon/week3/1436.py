N = int(input())
first = 666
while N != 0: # N 이 0이 아니면 계속 반복
    if '666' in str(first): # 만약 666이란 문자열이 first안에 있으면
        N = N-1
        if N == 0:
            break #반복문 나오기
    first = first + 1 #first의 값을 1 증가
print(first)