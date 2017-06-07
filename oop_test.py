# random variable generator
import random
# urllib - open an arbitrary URL
# urlopen - Create a file-like object for the specified URL to read from
from urllib.request import urlopen
# this module provides access to some objects used or maintaines by the
# interpreter and to functions that interact stringly with the interpreter.
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self, *** parameters.",
    "class %%%(object):\n\tdef ***(self,@@@)":
        "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, and call it with parameters self, @@@",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
# len - returns the number of elements
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
# append(adds) - append object to end
# strip(remove) - returns a copy of the string in which all chars have
#   have been stripped from the beginning and the end of the string
#   (default whitespace characters)
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))

def convert(snippet, phrases):
    # sample(population, k) - return a k length list of unique elements chosen
    #   from the population sequence. Used for random sampling whithout replacement
    # capitalize - returns a copy of the string with on;y its first character
    #   capitalized
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        # randint - returns a random integer
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        # [:] - effectively make a slice from the very first element to the
        #   very last one
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# keep going until they hit CTRL - C
try:
    while True:
        # keys() - returns a list of all the available keys in the dictionary
        snippets = list(PHRASES.keys())
        # shuffle - shuffle the sequence x in place.
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print(f"ANSWEAR: {answer}\n\n")
# EOFError - Raised when one of the built-in functions(input() or raw_input())
#   hits an end-of-file condition (EOF) without reading any data.
except EOFError:
    print("\nBye")
