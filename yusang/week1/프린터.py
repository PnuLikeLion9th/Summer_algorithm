#원하는 작업이 몇 번째에 있는지 파악
#제공된 배열에 push, pop 사용
#pop(0) 이후 목록에서 이것보다 큰게 있는지 검사
#있다면 push(), 없다면 다음


def solution(priorities, location):    
    count = 0 #횟수
    
    while 1: #조건 만족시까지 무한 반복
        #작업을 꺼냄
        x = priorities.pop(0)
     
        #작업보다 우선순위가 높은 것을 filter
        if len(list(filter(lambda n : n > x, priorities))) > 0 :
            #0 보다 크다면 맨뒤로 다시 push
            priorities.append(x)
            #원하는 작업의 위치를 옮겨줌
            if location == 0:
                location = len(priorities) -1
            else:
                location = location -1
        else:
            #우선순위가 정상이라면
            count = count + 1
            #횟수 증가
            #원하는 작업의 위치 변경
            if location == 0:
                return count
            else:
                location = location - 1

print(solution([2, 1, 3, 2], 2))