def solution(a,b):
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    date = ["FRI","SAT","SUN","MON","TUE","WEN","THU"]
    sum_day = sum(month[:a-1])+b#a달 전까지의 달 더하고 일수를 더함
    return date[sum_day%7-1]#나머지일수 구해주고 인덱스값이니까 -1빼줌

solution(5,24)