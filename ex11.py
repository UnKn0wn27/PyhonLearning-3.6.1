#raw_input() presents a prompt to the user(the optional arg of raw_intput([arg])
#gets input from the user and returns the data input by the user in a string.
#Exemple:
# name = input("What is your name?")
# print("Hello, {name}.")
print("How old are you?", end=' ')
age = input()
print("How tall are you", end=' ')
height = input()
print("How much do you weight?", end = ' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
