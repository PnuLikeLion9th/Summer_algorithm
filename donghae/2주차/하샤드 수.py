def solution(x):
    x_list = list(map(int, str(x)))  #문자열 x를 숫자 리스트로 변환
    sum = 0
    for i in range(len(x_list)):
        sum += x_list[i]    #자릿수의 합
    return x % sum == 0     #비교 연산자로 결괏값 출력