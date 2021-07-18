a, b = map(int, input().split()) 
#split의 결과를 매번 int로 변환해주려니 귀찮아서 map을 함께 사용
#map에 int와 input().split()을 넣으면 split의 결과를 모두 int로 변환해줌


while not (a == 0 and b == 0): 
    if a > b:
        print("Yes")
    else:
        print("No")
    a, b = map(int, input().split())