#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    num = 0
    roman_keys = list(roman_numerals.keys())
    skip = False
    for i in range(len(roman_string)):
        if skip:
            skip = False
            continue
        x = roman_string[i]
        if x not in roman_numerals:
            return 0
        try:
            y = roman_string[i + 1]
            idx_x = roman_keys.index(x) 
            # Check for (e.g. IX, XC, condition)
            if y == roman_keys[idx_x + 1] or y == roman_keys[idx_x + 2]: 
                num += (roman_numerals.get(y) - roman_numerals.get(x))
                # Skip the next element in the string
                skip = True
        except IndexError:
            pass
        # If there's no IX, XC condition, add roman numeral elements normally
        if not skip:
            num += roman_numerals.get(x)
    return num
