# 원소를 다 소문자화 시켜버리면, 출력할때 기존의 문자가 뭐였는지 잃게 된다. 기존의 문자를 기억시켜둘수있다면 가능

# 각 원소를 다른 변수에 할당, 변수[0]을 소문자화..? 겹쳐버리면 판별 불가능 ( x )
# Cat, fat, bAt, bAT

# 그냥 sort하면 대문자 쫙, 그 담에 소문자 쫙
# 그럼 원형을 일단 저장시키고, 모두 소문자화, 그런 다음 첫 놈 골라내고, 그놈의 원형을 찾자 -> 딕셔너리 사용
while True:
    Num = int(input())
    if Num == 0:
        break
    lis = dict()
    temp_dict = dict()
    for _ in range(Num):
        word = input()
        lis[word] = word
    temp_list = list()
    for v in lis.values():
        # v_origin = v
        temp_dict[v.lower()] = v

        # v = v.lower()
        temp_list.append(v)
    what = sorted(temp_dict.keys())
    print(temp_dict[what[0]])