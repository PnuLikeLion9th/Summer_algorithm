#2016년 해보쟈 ~~

def solution(a,b):
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = day[(sum(mon[:a-1])+b-1)%7] 
    return answer
