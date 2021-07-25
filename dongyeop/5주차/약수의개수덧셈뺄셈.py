# def solution(left, right):
#     decimal = list()
#     check= list()
#     answer=0
#     for i in range(left,right+1):
#         for j in range(1,i+1):
#             if i%j==0:
#                 decimal.append(j)
#         check.append(len(decimal))
#         decimal=list()
    
#     for i in range(len(check)):
#         if check[i]%2==0:
#             check[i] = '+'
#         else:
#             check[i] = '-'
    
#     for i in range(left,right+1):
#         if check[i-left] == "+":
#             i=i
#         else:
#             i=-i
#         answer+=i
#     return answer
#위에가 예전에 푼거.그냥 바로 빼거나 더하면 되는데 왜 저랬지..?
def solution(left,right):
    answer=0
    for i in range(left,right+1):#범위
        count = 0
        for j in range(1,i+1):#약수의 개수 구하기
            if i%j==0:
                count+=1
        if count%2==0:#약수의 개수가 짝수이면
            answer+=i#더해주고
        else:
            answer-=i#홀수이면 빼줌
    return answer