# 프로그래머스_2016년_수학_레벨 1
# 조건문 하나하나씩 넣으면 시간이 오래 걸릴 거 같아서 함수를 사용하여 간단히 풀었다.
# weekday 함수는 해당 날짜의 요일을 숫자로 반환한다 (월,화,수...,토,일 ==> 0,1,2...,5,6) 

import calendar

def solution(month, day):
    week_day = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    return week_day[calendar.weekday(2016,month,day)]

print(solution(1,1))