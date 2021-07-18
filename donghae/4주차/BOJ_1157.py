s = list(input().upper())
count={}    #중복 횟수를 담을 딕셔너리
for i in s:
    try: count[i] += 1
    except: count[i]=1
l = list(count.values()) #value값만 리스트 l로 정의
if l.count(max(l)) > 1: #max값이 2이상이면 '?'출력
    print('?')
else:   #아니면 value값이 max일 때 key값 출력
    for key, value in count.items():
        if value==max(count.values()):
            print(key)