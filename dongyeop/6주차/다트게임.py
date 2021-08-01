# def solution(dartResult): 예전에푼거
#     answer = 0
#     stack = list()
#     check_int = ""
#     for i in dartResult:
#         if i == "S":
#             stack.append(int(check_int))
#             check_int = ""
#             continue
#         elif i == "D":
#             stack.append(int(check_int))
#             check_int = ""
#             stack[-1]=stack[-1]**2
#         elif i == "T":
#             stack.append(int(check_int))
#             check_int = ""
#             stack[-1]=stack[-1]**3
#         elif i =="*":
#             if len(stack) == 1:
#                 stack[-1] = stack[-1]*2
#             elif len(stack) >1:
#                 stack[-1]=stack[-1]*2
#                 stack[-2]=stack[-2]*2
#         elif i == "#":
#             stack[-1] = stack[-1]*-1
#         else:
#             check_int+=i
    
#     answer= sum(stack)
#     return answer




import math
def solution(dartResult):
    # 3번의 기회
    # s d t 1 2제곱 3제곱
    # 에스터리스크 해당점수와 해당점수 바로전 점수 2배
    # 샵 해당점수 마이너스
    # 첫번째로 에스터리스크 나왔을경우 해당 점수만 2배
    # 스타상 중첩시 중첩된 점수 4배
    # 아차상과 중첩시 마이너스2배
    scorestack = []
    sdt = ['S','D','T']
    special = ['*','#']
    stay = ''#10때문에 만듬
    for i in dartResult:
        if i.isdigit():
            stay+=i
            continue
        if i in sdt:
            scorestack.append(stay)
            stay = ''
            if i == sdt[0]:
                scorestack[-1] = int(scorestack[-1])
            elif i == sdt[1]:
                scorestack[-1] = math.pow(int(scorestack[-1]),2)
            elif i == sdt[2]:
                scorestack[-1] = math.pow(int(scorestack[-1]),3)
        elif i in special:
            if i == special[0]:
                try:
                    scorestack[-2] = scorestack[-2]*2
                    scorestack[-1] = scorestack[-1]*2
                except:
                    scorestack[-1] = scorestack[-1]*2
            elif i == special[1]:
                scorestack[-1] = -1*scorestack[-1]
    return sum(scorestack)
                