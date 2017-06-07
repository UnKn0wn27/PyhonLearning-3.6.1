def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def substract(a, b):
    print(f"Substract {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiply {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Divide {a} / {b}")
    return a / b

print("Lets do some math with these functions")

age = add(30, 5)
height = substract(78, 4)
weigth = multiply(90, 2)
iq = divide(100, 2)

print(f"age: {age}, height: {height}, weigth: {weigth}, iq: {iq}")

# A puzzle for extra credit, type it in anyway
print("Here is a puzzle.")

#what = add(age, substract(height, multiply(weigth, divide(iq, 1))))

me = substract((add(24,(divide(34, 100)))), 1023)

print("That becomes: ", me, "Can you do it by hand?")
