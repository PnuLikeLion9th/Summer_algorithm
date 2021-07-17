def solution (a,b):
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"] #리스트에 요일 담고
    month = [31,29,31,30,31,30,31,31,30,31,30,31]  #해당 month까지 일수 다 더함
    return days[(sum(month[:(a-1)])+b)%7-1] # 다 더하고 나머지와 리스트 인덱싱 활용해서 요일 도출