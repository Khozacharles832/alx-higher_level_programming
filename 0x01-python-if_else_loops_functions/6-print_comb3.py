#!/usr/bin/python3
for i in range(0,10):
    for l in range(1,10):
        if i >= l:
            continue
        elif i == 8 and l == 9:
            print("{}{}".format(i,l))
        else:
            print("{}{}, ".format(i,l), end = "")
