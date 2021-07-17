def solution(a, b):
    d = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    month_days=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days= 0
    
    for i in range(a-1):                   # 해당 월을 제외한 월까지 날짜 수 더하기 (a로 잡으면 해당 월까지 계산해서 오류)
        total_days += month_days[i]
        
    total_days += b                        # 입력된 날짜까지 일 더하기
    day = (total_days+4) % 7               # 시작이 금요일이었으므로, total_days에 +4 더하기
    return d[day]