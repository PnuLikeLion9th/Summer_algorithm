#자릿수 더하기

'''전략1: 일단 숫자들을 다 문자로 바꾼 다음에, for문을 사용해서 
          문자를 다시 숫자로 바꾸면서 0위치의 숫자부터 부터 끝까지 다 더해줄거임!'''

def solution(n): 
    answer = 0 #일단 변수 0으로 지정해주기
    a = str(n) #str함수로 숫자 문자로 바꿔줌
         
    for i in range(len(a)):  # 0부터 a의 길이까지 순서대로 i에 대입하기 
        answer += int(a[i])  # 첫번째 자리값부터 끝까지 다 더하기
          
    return answer


'''전략2: 이번에는 while써봄. L이라는 위치변수 넣어줘서 L이 숫자 자릿수보다 넘어설때까지 각 자릿수 더하게 함'''

def solution(n):
    answer = 0
    L = 0      #위치변수 넣음
    a = str(n) #전략1이랑 똑같음
    
    while L < len(a) :  # 위치변수값이 a길이 넘기 전까지 반복, 파이썬은 위치가 0부터 시작하기 때문!
          answer += int(a[L]) # 첫번째 자리값부터 하나씩 더함 
          L += 1        # 한번 반복할때마다 위치변수에 1씩 더해줌
    
    return answer


