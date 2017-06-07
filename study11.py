def ultra(marine):
    print(f"Marine: {marine}")
# 1
ultra(1)
# 2
marine = 2
ultra(marine)
# 3
ultra(1 + 2)
# 4
ultra(marine + 2)
# 5
marine2 = int(input())
ultra(marine2)
# 6
ultra(int(input()))

# 7
marine3 = 5
ultra(marine + marine3)

# 8
word = "ultraman"
ultra(len(word))

# 9
ultra(9.6)

# 10
nr = int(open('number.txt').read())
ultra(nr)
