def solution(numbers, hand):
    keypad ={1: [0, 0], 2: [0, 1], 3: [0, 2],   #키패드 좌표로 만들기
             4: [1, 0], 5: [1, 1], 6: [1, 2],
             7: [2, 0], 8: [2, 1], 9: [2, 2],
             '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    L = keypad['*']     #시작지점
    R = keypad['#']
    res = ''    #결과 문자열
    for num in numbers:
        key = keypad[num]   #num에 해당하는 키패드 좌표값
        if num in [1,4,7]:  #1,4,7이면 왼손
            res += 'L'
            L = key
        elif num in [3,6,9]:   #3,6,9면 오른손
            res += 'R'
            R = key
        else:   #2,5,8,0인 경우
            L_dis = 0   #거리를 담을 변수 정의
            R_dis = 0
            for l,r,k in zip(L, R, key):    #zip함수 사용해서 좌표 계산
                L_dis += abs(l-k)
                R_dis += abs(r-k)
            if L_dis < R_dis:   
                res += 'L'
                L = key
            elif L_dis > R_dis:
                res += 'R'
                R = key
            else:   # 좌표 거리가 같은 경우
                if hand == 'left':
                    res += 'L'
                    L = key
                else:
                    res += 'R'
                    R = key
    return res