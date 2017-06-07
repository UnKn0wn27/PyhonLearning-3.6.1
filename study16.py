from sys import argv, exit
from textwrap import dedent
script, file_txt = argv

txt = open(file_txt)

def path():
    print(dedent("""
          This is your first mission as a normal soldier.
          Your dream is to become a Space Marine.
          You see 3 enemies.
          """))
    enemies = 3
    print("What do you do.")

    while True:
        choice = input("> ")
        if choice == "shoot enemies":
            print("You start to fire like a maniac and get wounded.")
            wounded()
        elif choice == "take cover":
            print("You took cover. What now?")
        elif choice == "take one down" and enemies == 3:
            print("You took one enemy down.")
            print("They are looking for you.")
            enemies -= 1
        elif choice == "change cover" and enemies == 2:
            print("You change cover. The enemies spoted you. What now?")
        elif choice == "throw a flashbang" and enemies == 2:
            print("You threw a flashbang and blinded the enemies.")
            print("You then were able to shoot them bouth.")
            enemies -= 2
            victory()
        else:
            print(f"You can't '{choice}' .")

def wounded():
    print("You wake up in the enemy headquarter.")
    print("You learn that the men who shoot you are called: Bob,Lee,Yu")
    enemies = ['Bob', 'Lee', 'Yu']

    print(dedent("""
          You are stranded to a chair.
          A light vision apears in front of you and a Chaos Gods says:
          Swear loyalty to me and i will set you free.
          """))
    bob = True
    lee = True
    yu = True
    answear = True
    print("What is your anwear?")
    while answear:
        choice = input("> ")
        if choice == "i swear":
            answear = False
        else:
            exit("You remained loyal to the Emperor!")
    print("You feel huge power rising in your body and a urge to kill something.")
    print("There are 3 enemies who do you want to take out first?")


    for remain in range(1, 4):
        print(enemies)
        choice = input("> ")
        if choice == "Bob" and bob:
            remain -= 1
            print(f"You killed Bob. There are now {remain} enemies")
            enemies.remove('Bob')
            bob = False
        elif choice == "Lee" and lee:
            remain -= 1
            print(f"You killed Lee. There are now {remain} enemies")
            enemies.remove('Lee')
            lee = False
        elif choice == "Yu" and yu:
            remain -= 1
            print(f"You killed Yu. There are now {remain} enemies")
            enemies.remove('Yu')
            yu = False
        else:
            print("Try again.")
    final2()
    exit(0)

def victory():
    print(dedent("""
                 After succesfully infiltrating the base!
                 You are faced with the great evil boss!
                 You have 10 seconds to kill him and difuse the bomb
                 What do you do?
                 """))

    boss_hp = 100
    your_hp = 100
    for i in range(10):
        print("Seconds past:", i + 1)
        print(f"Boss HP: {boss_hp}")
        print(f"Your HP: {your_hp}")
        choice = input("> ")

        if choice == "shoot him" and your_hp > 0 and boss_hp > 0:
            print("You shoot the boss -30 hp")
            boss_hp -= 30
            print("He shoots back -40 hp")
            your_hp -= 40
        elif choice == "throw granade" and your_hp > 0 and boss_hp > 0:
            print("You threw a granade at the boss -40 hp")
            boss_hp -= 40
            print("He rolled after the explosion and punched you in the face -20 hp")
            your_hp -= 20
        elif choice == "cut him" and your_hp < 0 and boss_hp < 0:
            print("You cut the boss -20")
            boss_hp -= 20
            print("He cuts you back -50")
            your_hp -= 50
        elif choice == "difuse bomb" and boss_hp > 0:
            print("The boss impales you from behind -100 hp")
            your_hp -= 100
        elif choice == "difuse bomb" and boss_hp <= 0:
            print("You difused the bomb!")
            final1()
            exit(0)
        elif your_hp <= 0:
            exit('You are dead...May the Emperor protect us now!')
        else:
            print("You are wasing time!")

def final1():
    print("You were victorious!")
    print("Mission succesfull!")

    line = txt.readlines()

    print("You became a", line[0])

def final2():
    print("You were victorious!")
    print("Blood for the blood god!")
    print("Skulls for the skull throne!")

    line = txt.readlines()

    print("You became a", line[1])

path()
