#!/usr/bin/python3

#Loop through ASCII values for lowercase alphabets
for alp in range(ord('a'), ord('z') + 1):
    #Print each alphabet without any newline
    print(chr(alp), end='')
