#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10
print('Last digit of', end=' ')
if last_digit > 6:
    print(number, 'is', last_digit, 'and is greater than 6')
elif last_digit == 0:
    print(number, 'is', last_digit, 'and is 0')
else:
    print(number, 'is', last_digit, 'and is less than 7 and not 0')
