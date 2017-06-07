formatter = "{} {} {} {}"

#this awesome
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))

# the single qoute in didn't will display with " " in terminal
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "I had this thing.",
    "That you could type right.",
    "But it didn't sing.",
    "So i said goodnight."
))
