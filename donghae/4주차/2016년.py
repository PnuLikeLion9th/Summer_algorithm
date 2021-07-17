def solution(a, b):
    day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  #달의 마지막 날짜를 리스트로 정의
    d = 5   #1월 1일은 금요일
    sum = 0
    for i in range(0, a-1): #지난달까지의 날짜 합을 for문으로 계산
        sum += mon[i]
    return day[(d+sum+b)%len(day)-1]    #범위를 벗어나지 않게 %len(day)