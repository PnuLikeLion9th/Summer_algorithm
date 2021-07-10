def solution(n):
    new = str(n) #n을 문자로 바꿔서 new로 저장
    add = 0
    for i in range(len(new)): #new의 길이 만큼 반복하는 i, 그동안 n의 i 인덱스 값을 add에 계속 더해줌
        add += int(new[i]) #더할 때는 int로 바꿔줘야 연산가능
    return add