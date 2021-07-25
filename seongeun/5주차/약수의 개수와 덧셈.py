#약수의 개수와 덧셈
'''전략: left부터 하나하나 약수 구해서 약수의 개수가 짝수면
        answer라는 새로운 리스트에 양수로 추가, 홀수면 -붙여서 추가한 뒤에
        요소 다 더해서 return '''

def solution(left, right):
    answer = []  #새롭게 담아줄 리스트 미리 만들기
    for i in range(right-left+1) : #0부터 right-left+1까지 i 넣어줌, 즉 left부터 right까지 숫자 각각의 약수의 개수 구해줄것임                                 
        b = [] #약수 담아줄 리스트 만들기
        c = 1  #위치변수 1로 잡기
        while c <= (left+i) : #left+i가 될때까지 반복
            if (left+i) % c == 0 : #만약 나머지가 0이라면
                b.append(c)   #약수니까 c를 리스트에 넣어줌
                c += 1        #위치변수에 1추가
            else :
                c += 1      #나머지 0아니면 그냥 위치변수에 1만 추가
        if len(b) % 2 == 0:  #약수의 개수가 짝수값이면
            answer.append(left+i) #answer라는 리스트에 그냥 숫자 추가

        else :               #약수의 개수가 홀수값이면
            answer.append(-(left+i)) #answer라는 리스트에 -숫자 추가

    return sum(answer) #answer 요소 다 더해서 return

