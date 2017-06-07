def while_function():
    i = 0
    n = 9
    numbers = []

    while i < n:
        print(f"At the top i is {i}")
        numbers.append(i)

        m = int(input("Nr > "))
        i += m
        print("Numbers now: ", numbers)
        print("At the bottom i is {i}")

while_function()


def for_function():
    numbers = []

    for i in range(1,6):
        print(f"At the top i is {i}")
        numbers.append(i)

        i += 1
        print("Numbers now: ", numbers)
        print(f"At the buttom i is {i}")

for_function()
