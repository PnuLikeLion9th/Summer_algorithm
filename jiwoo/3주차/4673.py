num = list(range(1,10001))
remove_list = []   # 셀프 넘버들 저장할 리스트

for i in num:
    n = i + sum(int(k) for k in str(i))   # 셀프 넘버 구하기
    if n <= 10000:
        remove_list.append(n)   # 10000 이하인 셀프 넘버 remove_list에 추가
    
for j in set(remove_list):  # set을 이용해 중복 제거
    num.remove(j)  # num 리스트에서 셀프 넘버 제거

for k in num:
    print(k)