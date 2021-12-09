# You are given a string and your task is to swap cases. In other words,
# convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    swapped_string = ""
    for letter in s:
        if letter.islower():
            swapped_string += letter.upper()
        else:
            swapped_string += letter.lower()
    return swapped_string
