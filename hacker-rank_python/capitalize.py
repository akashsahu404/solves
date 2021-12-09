# You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
# For example, alison heck should be capitalised correctly as Alison Heck.

# Given a full name, your task is to capitalize the name appropriately.
# The string consists of alphanumeric characters and spaces.
# Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.


def solve(s):
    final_name_list = []
    name_list = s.split(" ")
    for i in name_list:
        if len(i) > 0:
            if i[0].isdigit():
                final_name_list.append(i)
            else:
                final_name_list.append((i[0].upper() + i[1:len(i)]))
        if len(i) == 0:
            final_name_list.append(i)
    final_name = " ".join(final_name_list)
    return final_name
            
