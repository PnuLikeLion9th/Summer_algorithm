#다트게임


def solution(dartResult):
    dart = list(dartResult) 
    score = [] 
    
	# 문자열 -> 리스트 처리
    for i in range(len(dart)):
        if dart[i] == '1' and dart[i+1] == '0':
            score.append('10')
        elif dart[i] == '0' and dart[i-1] == '1':
            continue
        else:
            score.append(dart[i]) 
	
    # 다트게임 시작
    a = [] # 결과 담을 list 미리 생성
    
    for s in score:
        if s.isdigit(): 
            num = int(s)
        elif s.isalpha(): 
            if s == 'S':
                num = num ** 1
                a.append(num) 
            elif s == 'D':
                num = num ** 2
                a.append(num)
            elif s == 'T':
                num = num ** 3
                a.append(num)
                
		# *, # 처리
        if s == '*': 
            if len(a) >= 2: 
                a[-1] = a[-1] * 2
                a[-2] = a[-2] * 2
            else: 
                a[-1] = a[-1] * 2
                
        if s == '#': 
            a[-1] = a[-1] * (-1)

    return sum(a) 