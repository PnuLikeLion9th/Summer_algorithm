#2016
'''전략 python에 datetime이라는 라이브러리 이용!'''


from datetime import datetime

def solution(a,b):
    calender = datetime(2016, a, b) 
    c = ['MON','TUE','WED','THU','FRI','SAT','SUN'] #요일 목록 필요

    return c[calender.weekday()] #weekday(): 월요일부터 일요일까지 0~6으로만 표현