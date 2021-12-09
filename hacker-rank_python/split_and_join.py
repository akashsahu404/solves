# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

def split_and_join(line):
    string = line.split(" ")
    result = "-".join(string)
    return result
