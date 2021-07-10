def change(s):
    return s.replace("C#", "1").replace("D#", "2").replace(
        "F#", "3").replace("G#", "4").replace("A#", "5")


def solution(m, musicinfos):

    correct = []

    index = 0

    m = change(m)

    for music in musicinfos:
        music = music.split(',')

        # 시간 계산
        hours = int(music[1].split(':')[0]) - int(music[0].split(':')[0])
        minutes = int(music[1].split(':')[1]) - int(music[0].split(':')[1])
        countOrignal = hours * 60 + minutes
        count = hours * 60 + minutes

        music[3] = change(music[3])
        temp = music[3]

        while len(music[3]) < countOrignal and count > 0:
            music[3] = music[3] + temp
            count = count - len(temp)

        music[3] = music[3][:countOrignal]

        if m in music[3]:
            correct.append([countOrignal, music[2], index])
            index = index + 1

    if correct:
        correct.sort(key=lambda x: (-x[0], x[2]))
        return correct[0][1]

    else:
        return "(None)"


print(
    solution("CC#BCC#BCC#BCC#B", ["03:30,04:00,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
