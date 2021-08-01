# 스택 : 데이터를 효율적으로 저장하기 위한 자료로, 후입선출.

def solution(dartResult):
    stack = []
    dartResult = dartResult.replace("10", "A")      # 점수에 해당하는 숫자는 0~10 / 10은 두자리이기 때문에 예외 처리 -> 10을 다른 문자인 A로 바꾸기
    bonus = {'S': 1, 'D': 2, 'T': 3}                # S,D,T는 각각 1제곱, 2제곱, 3제곱 / 이 값을 딕셔너리로 관리
    
    for i in dartResult:
        if i.isdigit() or i=='A':
            stack.append(10 if i == 'A' else int(i))
        elif i in ('S', 'D', 'T'):
            num = stack.pop()
            stack.append(num ** bonus[i])
        elif i == '#':
            stack[-1] *= -1
        elif i == '*':
            num = stack.pop()
            if len(stack):
                stack[-1] *= 2
            stack.append(2 * num)
    return sum(stack)