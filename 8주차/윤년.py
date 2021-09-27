#백준 파이썬 기초 50제

'''윤년은 연도가 4의 배수이면서 100의 배수가 아니어야 한다. 하지만 예외적으로 400의 배수일 때는 윤년이다'''

A = input()
year= int(A)

if (year%4 == 0 and year%100!=0) or year%400==0:
    print('1')

else:
    print('0') 
