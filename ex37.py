import sys

print("\nand keyword")
if True and True:
    print("True")

print("\nas keyword")
with open("test.txt") as f:
    print(f.read())

print("\nassert keyword")
assert 2 + 2 == 4, "Houston we've got a problem"

print("\nbreak keyword")
for letter in 'Python':
    if letter == 'h':
        break
    print('Current letter:', letter)

print("\nClass keyword")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def display(self):
        print("Name:", self.name, "Salary: ", self.salary)
emp1 = Employee("Zara", 2000)
emp1.display()

print("\nContinue keyword")
for letter in 'Python':
    if letter == "h":
        continue
    print("Current letter:", letter)

print("\ndel keyword")
string = ['one','two']
print(string)
del string[1]
print(string)

print("\nexcept keyword")
try:
    fh = open("teste.txt","w")
    fh.write("I am going to become a great programmer!")
except IOError:
    print("Error: can't find data or read file")
else:
    print("Writen content in the file successfully!")
    fh.close()

print("\nexec keyword")
program = 'a = 5\nb = 10\nprint ("Sum = ", a + b)'
exec(program)

print("\nfinally keyword")
try:
    f = open("test.txt", 'w')
finally:
    f.close()

print("\nglobal keyword")
def bob():
    global me
    me = "Batman"
    print(me)

bob()
print(me)

print("\nis keyword")
if 5 is 5:
    print('5')

print("\nlambda keyword")
g =  lambda x: x**2 + 2*x - 5
print(g(27))

print("\npass keyword")
for letter in 'Python':
    if letter == 'h':
        pass
        print('This is a pass block')
    print('Current Letter:', letter)

print("\nraise keyword")
def functionName(level):
    if level > 1:
        raise "invalid level"
functionName(-1)

print("\nyield keyword")
def func():
    yield 'i am'
    yield 'a programmer'
gen = func()

print(list(gen))

print("\ndict data type")
dict = {'Name' : 'Zara', 'Age': 7}
print("Name:", dict['Name'])
print("Age:", dict['Age'])

print("\nString escapes")
print("\\p\'r\"o\ag\br\fa\nm\rm\re\tr\v")
