#!/usr/bin/python3
def uppercase(str):
    for char_ in str:
        int_equivalence = ord(char_)
        if int_equivalence >= 97 and int_equivalence <=122:
            int_equivalence = int_equivalence -32
        print("{0:c".format(int_equivalence), end="")
        print()
