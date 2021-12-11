# You are given a string S.
# Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

# Output Format

# In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if S has any alphabetical characters. Otherwise, print False.
# In the third line, print True if S has any digits. Otherwise, print False.
# In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if S has any uppercase characters. Otherwise, print False.

S = input("Enter string: ")

flag = False
for letter in s:
    while letter.isalnum():
        flag = True
        break
print(flag)

flag = False
for letter in s:
    while letter.isalpha():
        flag = True
        break
print(flag)

flag = False
for letter in s:
    while letter.isdigit():
        flag = True
        break
print(flag)

flag = False
for letter in s:
    while letter.islower():
        flag = True
        break
print(flag)

flag = False
for letter in s:
    while letter.isupper():
        flag = True
        break
print(flag)
