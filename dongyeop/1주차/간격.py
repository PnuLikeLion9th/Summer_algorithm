# def solution(x,n):
#     answer=[]
#     for i in range(x,x*(n+1),x):
#         answer.append(i)
#     return answer
# range의 세번째 파리미터 값에 의해 간격이 생긴다.
# 위 처럼 풀었을 때 테스트케이스 8번에서 런타임에러가 발생하여 아래와 같이 풀었다.

def solution(x,n):
    answer = []
    for i in range(1,n+1):
        answer.append(i*x)#x만큼 늘어나게 만들어야함으로 x를 곱해줬다.
    return answer