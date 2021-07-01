
#백준 1541 잃어버린 괄호
#+,-로만 이루어진 식이 주어진다.임의로 괄호를 넣어 최소의값이 나오도록 하여라

n=list(input().split('-'))
s = sum(map(int,n[0].split('+')))
a=0
for i in range(1,len(n)):
    a+=sum(map(int,n[i].split('+')))
print(s-a)

#-가 나오는 순간부터 다시 -가 나오기전까지 괄호를 치면 된다.
#-를 기준으로 split을 해주었고 쪼개진 요소들을 '+'를 기준으로
#split하여 더해주었다.