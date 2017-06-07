from sys import argv

script, user_name, batman = argv
prompt = "> "

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
like = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
This is a line that has '{batman}' The Dark Knight in it.
Alright, so you sad {like} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
