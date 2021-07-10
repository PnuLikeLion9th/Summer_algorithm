#정수 제곱근판별
'''전략: if문을 써서 n의 제곱근이 n의 제곱근을 정수형으로 변환시켰을 때 값과 같으면 x + 1의 제곱 아니면 -1 return!'''

def solution(n):                #매개변수는 n
    answer = 0
    x = n **(1/2)               # **로 'x는 n의 제곱근이다' 표현해줌

    if x == int(x) :            #만약 x가 x를 정수형으로 변환한 값과 같다면
        answer = (x + 1) ** 2   # x+1을 제곱한 값을 answer로 정하기

    else :  #아니면
        answer = -1             # -1을 answer로 정하기
    
    return answer

#or

def solution(n):
    x = n **(1/2) 

    if x == int(x) :
        return ((x + 1) ** 2)

    else :
        return -1
#바로 return 입력해도 될듯!