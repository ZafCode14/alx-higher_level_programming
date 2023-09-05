#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if i >= 'a' and i <= 'z':
            i = chr(ord(i) - ord('a') + ord('A'))
        print(i, end='')
    print('')
