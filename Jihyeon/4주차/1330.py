A, B = map(int, input().split())   # 변수들을 정수로 전환
if A > B:                          # A가 B보다 큰 경우
    print('>')
elif A < B:                        # A가 B보다 작은 경우
    print('<')
else:                              # 그렇지 않은 경우
    print('==')