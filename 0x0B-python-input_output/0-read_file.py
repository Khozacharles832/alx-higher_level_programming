#!/usr/bin/python3
""" Reads a file and prints it to  STDOUT """


def read_file(filename=""):
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
