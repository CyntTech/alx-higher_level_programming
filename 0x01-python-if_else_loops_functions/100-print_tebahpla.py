#!/usr/bin/python3

for lowup in range(ord('z'), ord('a') - 1, -1):
    if lowup % 2 == 0:
        diff = 0
    else:
        diff = 32
    print('{}'.format(chr(lowup - diff)), end='')
