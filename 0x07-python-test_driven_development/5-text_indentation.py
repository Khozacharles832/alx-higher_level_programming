#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimiter in "?:.":
        words = text.split(delimiter)
        text = (delimiter + "\n\n").join([index.strip() for index in words])

    print(text)

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/5-text_indentation.txt")
