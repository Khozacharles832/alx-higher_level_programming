#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    r_digit = {'I': 1,'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    r_number = 0
    for i in range(len(roman_string)):
        if i > 0 and r_digit[roman_string[i]] > r_digit[roman_string[i - 1]]:
            r_number += r_digit[roman_string[i]] - 2 * \
                    r_digit[roman_string[i - 1]]
        else:
            r_number += r_digit[roman_string[i]]
    return (r_number)
