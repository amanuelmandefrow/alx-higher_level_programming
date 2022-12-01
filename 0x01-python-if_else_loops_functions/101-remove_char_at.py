#!/usr/bin/python3
def remove_char_at(str, n):
    strcpy = ""
    numElem = 0

    for c in str:
        numElem = numElem + 1
    if n > (numElem - 1) or n  < 0:
        return str

    for c in str:
        if c != str[n]:
            strcpy = strcpy + c

    return strcpy
