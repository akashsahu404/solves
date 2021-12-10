# Given a list of filenames, we want to rename all the files with extension hpp to the extension h. To do this,
# we would like to generate a new list called newfilenames, consisting of the new filenames. Fill in the blanks
# in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension


filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = filenames.copy()
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
for file in filenames:
    if "."+"hpp" in file:
        file_index = filenames.index(file)
        dot_index = file.index(".")
        new_name = file[:dot_index] + ".h"
        newfilenames[file_index] = new_name

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
