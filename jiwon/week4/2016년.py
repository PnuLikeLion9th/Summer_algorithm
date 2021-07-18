def solution(a, b):
    answer = 0
    days = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    months = [31, 29, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
    
    for i in range(a-1): #a 이전 달까지 일 수 모두 더하기
      answer += months[i] 
    
    answer += b-1 # b=1이 시작이니까 1빼주기
    answer = answer % 7
    
    return days[answer]