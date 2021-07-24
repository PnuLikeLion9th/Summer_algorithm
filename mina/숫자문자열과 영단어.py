

def solution(s):
    number_strings = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
                      'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for number in number_strings:
        if number in s:
            s = s.replace(number, number_strings[number]) #replace!!!!
    return int(s)