#이용할 개념
#크기가 작은 수에 대해 d(n)을 한번씩만 한 값을 보면 나중에 큰 수로 합쳐지는 걸 볼 수가 있다
#그래서 d(n)을 여러번 하기 보다 그냥 범위 내에서 한번씩만 처리해주고 거기에 없는 값을 찾아낸다.
list=[]
for i in range(1,10001):
    t=str(i)
    num = i+sum([int(t[k]) for k in range(0,len(t))])  #자릿수 숫자 더한 값
    list.append(num)

for j in range(1,10001):
    if j not in list:   #리스트에 없으면 print해라
        print(j)