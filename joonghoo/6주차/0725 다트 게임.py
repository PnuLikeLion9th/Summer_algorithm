# 프로그래머스_다트 게임_스택_레벨 1
# 숫자와 STD, *# 을 조건문을 통해 고려해준다. 이떄 숫자가 한자리수를 넘어갈때를 생각하여 문자열로 받다가 STD에서 계산할때 int형으로 바꾸어준다
# STD에서 *를 고려하여 list 형태로 값을 추가해주어서 *에서 i, i-1를 연산할수있게 해준다

import math


def solution(dartResult):
    result = []
    num = ''
    for i in range(len(dartResult)):
        if dartResult[i] == 'S' or dartResult[i] == 'D' or dartResult[i] == 'T':
            if dartResult[i] == 'S':  # S일때는 num ** 1
                result.append(int(num))

            elif dartResult[i] == 'D':  # D일때는 num ** 2
                result.append(math.pow(int(num), 2))

            else:  # T일때는 num ** 1
                result.append(math.pow(int(num), 3))

            num = ''  # 초기화하여 다음 숫자를 입력받을수 있게 한다

        elif dartResult[i] == '*' or dartResult[i] == '#':
            if dartResult[i] == '*':
                if len(result) == 1:  # 첫번째 다트에서 *이 나올경우는 첫번째 점수만 *2
                    result[0] *= 2
                else:  # 최근의 2개의 점수를 *2 해준다
                    result[-1] *= 2
                    result[-2] *= 2
            else:  # 일때 *-1
                result[-1] *= -1

        else:  # 숫자일 경우
            num += dartResult[i]

    return int(sum(result))  # 모든 점수의 합


print(solution("1D2S#10S"))
