# making tuples
directions = ('north','south','east')
verbs = ('go', 'kill', 'eat')
stops = ('the', 'in', 'of')
nouns = ('bear', 'princess')

# we get a word from the function scan
def get_tuple(inspect):
    word = inspect.lower()

    if word in directions:
        return('direction', word)
    elif word in verbs:
        return('verb', word)
    elif word in stops:
        return('stop', word)
    elif word in nouns:
        return('noun', word)
    elif word.isdigit():
        return('number', int(word))
    else:
        return('error', inspect)

def scan(sentence):
    # if the sentence has more words split them
    words = sentence.split()

    return [get_tuple(word) for word in words]
