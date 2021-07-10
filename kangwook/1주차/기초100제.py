#210621(월) 
#기초100문제!!

#6001
print("Hello")

#6002
print("Hello World")

#6003
print("Hello")
print("World")

#6004
print("'Hello'")

#6005
print('"Hello World"')

#6006
print("\"!@#$%^&*()'")
#출력용 따옴표는 백슬래쉬 \를 통해 구분한다.

#6007
print('"C:\\Download\\\'hello\'.py"')
#출력 문자에 백슬래쉬가 있을 경우 이 또한 백슬래쉬를 통해 출력용이라고 알려주어야 한다.

#6008
print('print(\"Hello\\nWorld\")')
#\n은 줄바꿈을 표시하는 태그이다. 이를 출력용이라 알려주기 위해 백슬래쉬를 앞에 하나 더 붙인다. 
#그리고 나머지 따옴표에도 백슬래쉬를 붙여준다.

#6009
k=input()
print(k)

#6010
k=input()
k=int(k)
print(k)
#입력한 변수k를 int라는 정수를 의미하는 변수로 받아주고 이를 print해준다.

#6011
k=input()
k=float(k)
print(k)
#실수는 float!

#210622 (화)

#6012
a=input()
b=input()
a=int(a)
b=int(b)
print(a)
print(b)

#6013
a=input()
b=input()
print(b)
print(a)

#210623
#6014
f=input()
print(f)
print(f)
print(f)

#6015
a,b = input().split()
#파이썬만 이렇게 한꺼번에 두가지 변수를 받을 수 잇음. 
#다른 언어는 a=1, b=2 이렇게 따로 받아야 함.
print(a)
print(b)

#6016
a,b = input().split()
print(b,a)
#공백을 두고 입력받으려면 split 안에 ''이 아니라 그냥 split()

#6017
k=input()
print(k,k,k)

#6018
a,b=input().split(':')
print(a,b,sep=":")

#6019
a,b,c=input().split(".")
print(c,b,a,sep="-")

#6020
a,b=input().split('-')
print(a+b)
#input 뒤에 split이 붙으면 input받은 걸 '-' 전 후로 두게를 나눈다는 뜻
#input은 하나지만 두 개가 돼서 print할 때 두개로 한다.

#6021
s = input()
for i in s:
    print(i)

#6022
date = input()
print(date[:2] + ' ' + date[2:4] + ' ' + date[4:])

#6023
#1
date = input().split(':')
print(date[1])
#2
a,b,c=input().split(':')
print(b)

#6024
a, b = input().split()
s = a + b
print(s)

#6025
a, b = input().split()
print('{}'.format(int(a)+int(b)))

#6026
a = float(input()) #input 받은 거를 바로 float로 선언해벌이기
b = float(input())
print('{}'.format(a + b))

#6027
print('%x'%int(input())) #print 안에다가 바로 input 넣어벌임

#6028
print('%x'.upper()%int(input()))

#6029
print('%o'%int(input(), 16))

#6030
print(ord(input()))

#6031
print(chr(int(input())))

#6032
print(-int(input()))

#6033
print(chr(ord(input())+1))

#6034
a, b = input().split()
print(int(a) - int(b))

#6035
a, b = input().split()
print(float(a) * float(b))

#6036
s = input().split()
for i in range(int(s[1])):
    print(s[0], end='')

#2
a,n=input().split()
print(a*int(n)) 
#문자를 여러번 반복하기 위해서는 정수 n번만큼 반복해야 한다고 말해줘야 한다
#그래서 n을 정수로 선언해주어야 한다!

#6037
count = int(input())
s = input()
print(s * count)
#어쩄든 반복하고 싶은 횟수를 정수로 지정해줘야 한다!

#6038
a, b = input().split()
print(int(a) ** int(b))

#6039
a, b = input().split()
print(float(a) ** float(b))

#6040
a, b = input().split()
print(int(a) // int(b))

#6041
a, b = input().split()
print(int(a) % int(b))

#6042
print(round(float(input()), 2))

#6043
a, b = map(float, input().split())
print('%.3f' %round((a / b), 3))

#6044
a, b = input().split()
a = int(a)
b = int(b)
if(a >= 0 and b != 0):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a // b)
    print(a % b)
    print(round((a / b), 2))

#6045
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
print(a + b + c, round(((a + b + c) / 3), 2))

#6046
print(int(input())<<1)

#6047
a, b = map(int, input().split())
print(a * (2 ** b))

#6048
a, b = map(int, input().split())
print(a < b)

#6049
a, b = map(int, input().split())
print(a == b)

#6050
a, b = map(int, input().split())
print(a <= b)

#6051
a, b = map(int, input().split())
print(a != b)

#6052
print(bool(int(input())))

#6053
print(not bool(int(input())))

#6054
a, b = map(int, input().split())
print(bool(a) and bool(b))

#6055
a, b = map(int, input().split())
print(bool(a) or bool(b))

#6056
a, b = map(int, input().split())
if (bool(a) != bool(b)):
    print(True)
else:
    print(False)

#6057
a, b = map(int, input().split())
if (bool(a) == bool(b)):
    print(True)
else:
    print(False)

#6058
a, b = map(int, input().split())
print(bool(a) is False and bool(b) is False)
#is 대신 == 을 써도 된다!

#6059
print(~int(input()))

#6060
a, b = map(int, input().split())
print(a & b)

#6061
a, b = map(int, input().split())
print(a | b)

#6062
a, b = map(int, input().split())
print(a ^ b)

#6063
a, b = map(int, input().split())
print(a if a > b else b)

#6064
a, b, c = map(int, input().split())
print((a if a < b else b) if (a if a < b else b) < c else c)

#6065
data = input().split()
for i in data:
    if(int(i) % 2 == 0):
        print(int(i))

#6066
data = input().split()
for i in data:
    if(int(i) % 2 == 0):
        print('even')
    else:
        print('odd')

#6067
data = int(input())
if(data % 2 == 0 and data < 0):
    print('A')
elif(data % 2 != 0 and data < 0):
    print('B')
elif(data % 2 == 0 and data > 0):
    print('C')
elif(data % 2 != 0 and data > 0):
    print('D')

#6068
score = int(input())
if(score >= 90):
    print('A')
elif(score >= 70):
    print('B')
elif(score >= 40):
    print('C')
elif(score >= 0):
    print('D')

#6069
grade = input()
if(grade == 'A'):
    print('best!!!')
elif(grade == 'B'):
    print('good!!')
elif(grade == 'C'):
    print('run!')
elif(grade == 'D'):
    print('slowly~')
else:
    print('what?')

#6070
month = int(input())
season = ''
if(month in [12, 1, 2]):
    season = 'winter'
elif(month in [3, 4, 5]):
    season = 'spring'
elif(month in [6, 7, 8]):
    season = 'summer'
else:
    season = 'fall'
print(season)

#6071
i = True
while(i):
    num = int(input())
    if(num == 0):
        i = False
    else:
        print(num)

#6072
num = int(input())
while(num > 0):
    print(num)
    num -= 1

#6073
num = int(input())
while(num > 0):
    num -= 1
    print(num)

#6074
a = input()
count = 0
while(count <= ord(a)-97):
    print(chr(97+count), end=' ')
    count += 1

#6075
n = int(input())
for i in range(n + 1):
    print(i)

#6076
n = int(input())
for i in range(n + 1):
    print(i)

#6077
n = int(input())
s = 0
for i in range(n + 1):
    if(i % 2 == 0):
        s += i
print(s)

#6078
c = ''
while(c != 'q'):
    c = input()
    print(c)

#6079
n = int(input())
i = 0
s = 0
while(s < n):
	i += 1
	s += i
print(i)

#6080
n, m = map(int, input().split())
for i in range(1, n + 1):
    for j in range(1, m + 1):
        print('{} {}'.format(i, j))

#6081
n = input()
for i in range(1, 15 + 1):
	print('%x*%x=%x'.upper() %(int(n, 16), int(hex(i), 16), (int(n, 16) * int(hex(i), 16))))

#6082
n = int(input())
for i in range(1, n + 1):
    if(i % 10 == 3 or i % 10 == 6 or i % 10 == 9):
        print('X', end = ' ')
    else:
        print(i, end = ' ')

#6083
a, b, c = map(int, input().split())
count = 0
for i in range(a):
	for j in range(b):
		for k in range(c):
			print('{} {} {}'.format(i, j, k))
			count += 1
print(count)

#6084
h, b, c, s = map(int, input().split())
mb = round((h * b * c * s / 8) / 1024 / 1024, 1)
print('{} MB'.format(mb))

#6085
w, h, b = map(int, input().split())
mb = round(((w*h*b) / 8 / 1024 / 1024), 2)
print('{:.2f} MB'.format(mb))

#6086
n = int(input())
total = 0
for i in range(1, n + 1):
    total += i
    if(total >= n):
        break
print(total)

#6087
n = int(input())
for i in range(1, n + 1):
    if(i % 3 == 0):
        pass
    else:
        print(i)

#6088
a, b, n = map(int, input().split())
total = a
for i in range(a, a + n - 1):
	total += b
print(total)

#6089
a, b, n = map(int, input().split())
total = a
for i in range(a, a + n - 1):
	total *= b
print(total)

#6090
a, m, d, n = map(int, input().split())
total = a
for i in range(a, a + n - 1):
	total = total * m + d
print(total)

#6091
a, b, c = map(int, input().split())
d = 1
while d % a != 0 or d % b != 0 or d % c != 0:
    d += 1
print(d)

#6092
from random import randint
n = int(input())
temp = [0] * 23
nums = input().split()
for i in nums:
    temp[int(i)-1] += 1
for i in temp:
    print(i, end=' ')

#6093
n = int(input())
nums = input().split()
nums.reverse()
for i in nums:
    print(int(i), end=' ')

#6094
n = int(input())
nums = map(int, input().split())
print(min(nums))

#6095
li = [[0 for i in range(19)] for j in range(19)]
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if(li[x-1][y-1] != 1):
        li[x-1][y-1] = 1
for i in li:
	print(' '.join(map(str, i)))

#6096
li = []
for i in range(19):
    li.append([])
    k = input().split()
    for e in k:
        li[i].append(int(e))
n = int(input())
x = []
y = []
for i in range(n):
    a, b = map(int, input().split())
    for j in range(19):
        li[a-1][j] = 1 if li[a-1][j] != 1 else 0
        li[j][b-1] = 1 if li[j][b-1] != 1 else 0
for i in li:
    print(' '.join(map(str, i)))

#6097
li = []
h, w = map(int, input().split())
for i in range(h):
	li.append([])
	for j in range(w):
		li[i].append(0)
n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    for j in range(l):
        if d == 0:
            li[x-1][y-1] = 1
            y += 1
        else:
            li[x-1][y-1] = 1
            x += 1
for i in li:
    print(' '.join(map(str, i)))

#6098
li = []
for i in range(10):
    li.append([])
    k = input().split()
    for e in k:
        li[i].append(int(e))
x, y = 1, 1
flag = True

while flag:
    if li[x][y] == 2:
        li[x][y] = 9
        flag = False
    elif (li[x][y+1]) == 1:
        if li[x+1][y] == 1:
            li[x][y] = 9
            flag = False
        else:
            li[x][y] = 9
            x += 1
    else:
        li[x][y] = 9
        y += 1
for i in li:
    print(' '.join(map(str, i)))