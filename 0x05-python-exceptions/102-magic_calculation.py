#!/usr/bin/python3

def magic_calculation(a, b):
    answer = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
        except:
            raise Exception('Too far')
        else:
            answer += a ** b / i
        answer += a + b
        return (answer)
