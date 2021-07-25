from collections import deque
n = int(input())

for i in range(n):
    m,n = map(int,input().split())
    i = deque(list(map(int,input().split())))
    index = deque(list(range(m)))              # 인덱스 값을 담은 리스트 생성
    f_index = index[n]                         # f_index에 초기 인덱스 값 담아줌
    count = 0
    
    while True:

        if i[0] == max(i) :                    # i[0] 의 중요도가 가장 높다면,

            if f_index == index[0] :           # 현재 앞에 있는 중요도의 인덱스 값과 초기 인덱스 값이 같다면!
                count += 1                     # 인쇄 순서 프린트해줌
                print(count)
                break
            else:                              # 구하고자 했던 값이 아님
                i.popleft()                   
                index.popleft()
                count += 1

        else:                                  # 중요도가 높은 문서가 뒤에 있다는 것
            i.append(i.popleft())
            index.append(index.popleft())