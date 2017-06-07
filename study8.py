from sys import argv

script, filename = argv

print("Open file")
txt = open(filename,'r')

print("Reading file")
print(txt.read())

print("Closing file")
txt.close()
