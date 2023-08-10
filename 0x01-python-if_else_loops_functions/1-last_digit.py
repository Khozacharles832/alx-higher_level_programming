#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
first = " and is greater than 5"
second = " and is 0"
third = " and is less than 6 and not 0"
if number < 0:
    last = number % -10
else:
    last = number % 10
if last > 5:
    print("Last digit of {} is {}".format(number, last) + first)
elif last == 0:
    print("Last digit of {} is {}".format(number, last) + second)
else:
    print("Last digit of {} is {}".format(number, last) + third)
