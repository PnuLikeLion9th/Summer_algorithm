def solution(a, b):
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']     # 2016년 1월 1일이 금요일부터 시작하니까 리스트의 시작을 FRI로 설정
    day = day*55                                          # 리스트 반복
    pattern = [0,31,29,31,30,31,30,31,31,30,31,30,31]     # 1월부터 12월까지의 일수를 담은 리스트
    
    answer = day[sum(pattern[:a]) + b-1]
    return answer

    # ****어랴와