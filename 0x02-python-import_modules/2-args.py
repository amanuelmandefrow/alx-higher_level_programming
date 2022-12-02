#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argv_count = len(argv)
    if argv_count == 0:
        print("{:d} arguments.".format(argv_count))
    elif argv_count == 1:
        print("{:d} argument:".format(argv_count))
        print("{:d}: {:s}".format(1, argv[1]))
    else:
        print("{:d} arguments: ".format(argv_count))
        for i in range (1, argv_count + 1):            
            print("{:d}: {:s}".format(i, argv[i]))
