print("""
You enter a dark room with two doors.
Do you go through the #1 or door #2 or #3?
""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake. What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better. Bear runs away.")
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Undestanding revolvers yellin melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powere by mind of jello. Good job.")
    else:
        print("The insanity rots your eyes into a pool of muck. Good job.")
elif door == "3":
    print("You see the God-Emperor of Mankind. What do you do?")
    print("1. Bow befor him.")
    print("2. Attack him.")

    emperor = input("> ")

    if emperor == "1":
        print("The emperor will make you a space marine!")
    elif emperor == "2":
        print("You heretic! DIE!")
    else:
        print("I don't know how but you have a heart attack and die.")

else:
    print("You stumble around and fall on a knife and die. Good job.")
