def solution(a, b):
    days=['FRI','SAT','SUN','MON','TUE','WED','THU']
    if a==1:
        monthdays=0
    elif a==2:
        monthdays=31
    elif a==3:
        monthdays=31+29

    elif a>=4 and a<=8 and a%2==0:
        monthdays=31*((a//2))+30*((a//2)-2)+29
    elif a>=4 and a<=8 and a%2==1:
        monthdays=31*((a//2))+30*((a//2)-1)+29

    elif a>=9 and a<=12 and a%2==0:
        monthdays=31*((a//2))+30*((a//2)-2)+29
    elif a>=9 and a<=12 and a%2==1:
        monthdays=31*((a//2)+1)+30*((a//2)-2)+29

    holedays=monthdays+b

    index=(holedays%7)-1

    return(days[index])