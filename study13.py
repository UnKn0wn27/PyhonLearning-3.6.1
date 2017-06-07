print("Calculate 2 numbers.")

nr1 = int(input("Nr1: "))
nr2 = int(input("Nr2: "))

print("Choose what equation you want to make.")
print("1. +")
print("2. -")
print("3. *")
print("4. /")

nr = int(input("Choose option: "))

if nr == 1:
    print(f"Answear: {nr1 + nr2}")
elif nr == 2:
    print(f"Answear: {nr1 - nr2}")
elif nr == 3:
    print(f"Answear: {nr1 * nr2}")
elif nr == 4:
    print(f"Answear: {nr1 / nr2}")
else:
    print("There is no such optionself.")
