n= input()
answer = []
change = 0
#다솜이는 연속된 숫자들은 뒤집을수있다.
#최소한 뒤집고 모두 같게 만들어야한다.
for i in n:
    if answer:
        if answer[-1] != i:
            answer.append(i)
            change+=1
    else:
        answer.append(i)
print((change+1)//2)
