#회의를 진행하는데 겹치는지 않아야하고 회의가 시작과 동시에 끝날수 있으며 종료시간과 시작시간은 겹칠수있음
n = int(input())
conference = []
for _ in range(n):
    a,b= map(int,input().split())
    conference.append([a,b])
conference.sort(key=lambda x: (x[1],x[0]))
end = 0
count = 0
for i in conference:
    if i[0]>=end:
        count+=1
        end = i[1]
print(count)