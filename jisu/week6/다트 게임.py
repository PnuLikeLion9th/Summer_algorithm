def solution(dartResult):
    stack = []
    bonus = {'S': 1, 'D': 2, 'T': 3}
    # 10은 Z로 임시 변경 ('1','0'으로 인식 방지)
    dartResult = dartResult.replace('10', 'Z')

    for i in dartResult:
        if i == 'Z':
            stack.append(10)
        elif i.isdigit():
            stack.append(int(i))
        elif i in ('S', 'D', 'T'):  # 보너스일 경우
            stack[-1] = stack[-1]**bonus[i]
        elif i == '*':  # 스타상
            num = stack.pop()
            if len(stack):
                stack[-1] *= 2
            stack.append(num*2)
        elif i == '#':  # 아차상
            stack[-1] *= -1

    return sum(stack)
