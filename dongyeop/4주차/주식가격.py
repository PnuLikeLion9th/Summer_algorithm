# 브루트포스
# def solution(prices):
#     answer=[0]*len(prices)
#     for i in range(len(prices)):
#         for j in range(i+1,len(prices)):
#             if prices[i] <=prices[j]:
#                 answer[i]+=1
#             else:
#                 answer[i]+=1
#                 break
#     return answer
def solution(prices):#스택
    length = len(prices)
    answer=[0]*length
    stack = list()
    for i,price in enumerate(prices):#가격들의 인덱스 값과 가격
        while stack and price<prices[stack[-1]]:#스택이 존재하고 현재값이 더 작으면
            index=stack.pop()#스택에서 빼주고
            answer[index]=i-index#현재 인덱스와 스택에 담겼던 녀석의 인덱스를 빼면 시간임
        stack.append(i)

    while stack:#반복문이 다돌고 아직 남아있는 스택을 비워준다.
        index=stack.pop()
        answer[index] = length-index-1

    return answer