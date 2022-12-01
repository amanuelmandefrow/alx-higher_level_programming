#!/usr/bin/python3
def islower(c):
    char_equivalence = ord(c)
    if(char_equivalence > 97 and char_equivalence < 127):
        return True
    else:
        return False
