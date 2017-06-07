ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

for i in range(len(stuff)):
    if len(stuff) == 10:
        break
    next_one = more_stuff.pop()
    print("Adding:", next_one)
    stuff.append(next_one)
    print("There are {len(stuff)} items now.")

print("There we go:", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) #whoa! fancy
# pop() = remove and return item at index (default last)
print(stuff.pop())
# join() = returns a string in which the string elements of sequence
# have been joined by str separator
print(' '.join(stuff)) #what? cool!
print('#'.join(stuff[3:5]))  #super stellar!
