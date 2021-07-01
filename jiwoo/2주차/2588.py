a= int(input())
b= input()

c= int(b[2])*a   # a와 b의 1의 자리 수 곱하기
d= int(b[1])*a   # a와 b의 10의 자리 수 곱하기
e= int(b[0])*a   # a와 b의 100의 자리 수 곱하기
f= a*int(b)

print(c,d,e,f, sep="\n")