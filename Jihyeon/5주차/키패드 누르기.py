def solution(numbers, hand):
    answer = ''
    

    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}               # 키패드 좌표료 변경
    
    left_s = dic['*']
    right_s = dic['#']
    
    for i in numbers:
        now = dic[i]

        if i in [1, 4, 7]:                                   # 1, 4, 7을 누르는 경우
            answer += 'L'                                    
            left_s = now                                     # 왼손
            
        elif i in [3, 6, 9]:                                 # 3, 6, 9를 누르는 경우
            answer += 'R'                                    
            right_s = now                                    # 오른손
            
        else:                                                # 2, 5, 8, 0을 누르는 경우
            left_d = 0
            right_d = 0
            
            for a, b, c in zip(left_s, right_s, now):        # 좌표 거리 계산해주기
                left_d += abs(a-c)
                right_d += abs(b-c)
            
            if left_d < right_d:                             # 왼손이 더 가까운 경우
                answer += 'L'
                left_s = now
                
            elif left_d > right_d:                           # 오른손이 더 가까운 경우
                answer += 'R'
                right_s = now
            
            else:                                            # 두 거리가 같은 경우
                if hand == 'left':                           # 왼손잡이인 경우
                    answer += 'L'
                    left_s = now
                    
                else:                                        # 오른손잡이인 경우
                    answer += 'R'
                    right_s = now
            
    return answer