print("Let's practice everything.")
print('You\'d nee to know \'bout escapes with \\ that do \n and \t tabs')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and required an explanation
\n\twhere the is none.
"""

print("----------------------------------")
print(poem)
print("----------------------------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")
#def can return multiple variables WOW TEHNOLOGY!
def secret_formulat(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formulat(start_point)

print("With a starting point of: {}".format(start_point))
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates")

start_point /= 10

print("We can also say like this:")
formula = secret_formulat(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates".format(*formula))
