import datetime  # weekday() 함수 사용을 위한 모듈 import


def solution(a, b):
    dates = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return dates[datetime.date(2016, a, b).weekday()]  # 2016년 a월 b일의 요일 반환
