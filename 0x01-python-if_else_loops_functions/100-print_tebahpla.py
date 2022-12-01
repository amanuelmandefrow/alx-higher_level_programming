#!/usr/bin/python
for i in range(122, 96, -1):
    if i % 2 == 0:
        print_char = chr(i)
    elif i % 2 ==1:
        print_char = chr(i - 32)
    print(print_char, end="")
