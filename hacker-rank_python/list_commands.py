# Consider a list (list = []). You can perform the following commands:

# 1. insert i e: Insert integer e at position i.
# 2. print: Print the list.
# 3. remove e: Delete the first occurrence of integer e.
# 4. append e: Insert integer e at the end of the list.
# 5. sort: Sort the list.
# 6. pop: Pop the last element from the list.
# 7. reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through 
# each command in order and perform the corresponding operation on your list.


N = int(input())
list = []
for i in range(N):
    command_list = input()
    list.append(command_list.split())
new_list = []
for command in list:
    if command[0] == "insert":
        new_list.insert(int(command[1]), int(command[2]))
    if command[0] == "print":
        print(new_list)
    if command[0] == "remove":
        new_list.remove(int(command[1]))
    if command[0] == "append":
        new_list.append(int(command[1]))
    if command[0] == "sort":
        new_list.sort()
    if command[0] == "pop":
        new_list.pop()
    if command[0] == "reverse":
        new_list.reverse()
        
        
        
# Input Demo
# -------------
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# Output Demo
# -------------
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]
