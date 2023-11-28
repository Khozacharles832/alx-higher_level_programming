#!/usr/bin/python3
'''Text indentation module'''


def text_indentation(text):
    '''Text indentation module'''
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for delim in '?:.':
        words = (delim + '\n\n').join(
                [index.strip('') for index in words.split(delim)])
if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/5-text_indentation.txt')
