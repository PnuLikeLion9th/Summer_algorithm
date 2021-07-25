def solution(numbers, hand):
    l = [1,4,7]
    r = [3,6,9]
    result = ''
    l_current = 10    # 왼손 시작은 *
    r_current = 12    # 오른손 시작은 #
    
    for i in range(len(numbers)):
        
        if numbers[i] in l:    # 왼쪽 열의 1,4,7 입력 시 왼손 사용
            result += 'L'
            l_current = numbers[i]
            
        elif numbers[i] in r:  # 오른쪽 열의 3,6,9 입력 시 오른손 사용
            result += 'R'
            r_current = numbers[i]
            
        else:
            if numbers[i] == 0:
                numbers[i] = 11
            
            l_abs = abs(l_current - numbers[i])   # 현재 위치와 원하는 숫자의 차
            r_abs = abs(r_current - numbers[i])
            
            if (l_abs%3 + l_abs//3) > (r_abs%3 + r_abs//3) :    # 오른손이 더 가까운 경우
                result += 'R'
                r_current = numbers[i]
            elif (l_abs%3 + l_abs//3) < (r_abs%3 + r_abs//3) :  # 왼손이 더 가까운 경우
                result += 'L'
                l_current = numbers[i]
            else:                                     # 원하는 숫자로 부터 왼손과 오른손의 거리가 같을 경우
                if hand == 'right':                   # 오른손잡이는 오른손으로
                    result += 'R'
                    r_current = numbers[i]
                elif hand == 'left':                  # 왼손잡이는 왼손으로
                    result += 'L'
                    l_current = numbers[i]
    
    return result