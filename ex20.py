from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

# The method seek() sets the fils's current position at the offset. the
# whence argument is optional and defaults to 0, which means absolute file
# pisiotioning, other values are 1 which means seek relative to the
# current position and 2 means seek relative to the files end.

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file: \n")
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
