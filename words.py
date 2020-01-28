import random

class letter():
    def __init__(self, name, factor):
        self.name = name
        self.factor = factor
        
class word():
    def __init__(self, name, typeis):
        self.name = name
        self.typeis = typeis


letters = [letter('a', int(81)), letter('b', int(15)), letter('c', int(27)), letter('d', int(43)), letter('e', int(120)), letter('f', int(23)), letter('g', int(20)), letter('h', int(59)), letter('i', int(73)), letter('j', int(1)), letter('k', int(7)), letter('l', int(40)), letter('m', int(26)), letter('n', int(70)), letter('o', int(77)), letter('p', int(18)), letter('q', int(1)), letter('r', int(60)), letter('s', int(63)), letter('t', int(91)), letter('u', int(29)), letter('v', int(11)), letter('w', int(21)), letter('x', int(2)), letter('y', int(21)), letter('z', int(1))]
sentence = ""
paragraph = ""

dictionary = []
nouns = []
verbs = []
articles = []
adjectives = []
adverbs = []
connectors = []


temp = ""
test = []
extra = ""

first = False

def newword():
    global letters
    global word
    global dictionary
    global extra

    new = []
    types = ['v', 'n', 'a', 'j', 'd', 'c']


    for i in range(1, 10):
        y = random.randint(1, 120)
        x = random.randint(0, len(letters)-1)

        if letters[x].factor > y:        
            new.append(letters[x].name)#RIGHT HERE MAYBE? FIX BLANK WORDS

    h = ""
    h = h.join(new)

    word.typeis = types[random.randint(0, 5)]
    word.name = h
    dictionary.append(word.name)

    extra = word.name

    if word.typeis == 'v':
        verbs.append(word.name)
    if word.typeis == 'n':
        nouns.append(word.name)
    if word.typeis == 'a':
        articles.append(word.name)
    if word.typeis == 'j':
        adjectives.append(word.name)
    if word.typeis == 'd':
        adverbs.append(word.name)
    if word.typeis == 'c':
        connectors.append(word.name)

def r_art():
    global articles
    global temp
    global first
    
    temp = articles[random.randint(0, len(articles)-1)]

def r_noun():
    global nouns
    global temp
    global first

    temp = nouns[random.randint(0, len(nouns)-1)]

    
def r_verb():
    global verbs
    global temp
    global first

    temp = verbs[random.randint(0, len(verbs)-1)]


def r_adj():
    global adjectives
    global temp
    global first

    temp = adjectives[random.randint(0, len(adjectives)-1)]


def r_adv():
    global adverbs
    global temp
    global first

    temp = adverbs[random.randint(0, len(adverbs)-1)]

    
def r_con():
    global connectors
    global temp
    global first

    temp = connectors[random.randint(0, len(connectors)-1)]

def capcheck():
    global first
    global temp
    
    if first == True:
        x = ""
        bruh = []

        for i in temp:
            bruh.append(i)
            bruh[0] = bruh[0].upper()

        x = x.join(bruh)
        temp = x

        first = False


def newsentencebase():
    global test

    x = random.randint(0, 4)

    if x == 0:
        test.append(" ")
        r_noun()
        capcheck()
        test.append(temp)

        test.append(" ")
        r_verb()
        capcheck()
        test.append(temp)

    if x == 1:
        test.append(" ")
        r_noun()
        capcheck()
        test.append(temp)

        test.append(" ")
        r_verb()
        capcheck()
        test.append(temp)

        test.append(" ")
        r_noun()
        capcheck()
        test.append(temp)
        
    if x == 2:
        test.append(" ")
        r_noun()
        capcheck()
        test.append(temp)

        test.append(" ")
        r_verb()
        capcheck()
        test.append(temp)

        test.append(" ")
        r_adj()
        capcheck()
        test.append(temp)
        
    if x == 3:
        test.append(" ")
        r_noun()
        capcheck()
        test.append(temp)

        test.append(" ")
        r_verb()
        capcheck()
        test.append(temp)

        test.append(" ")
        r_adv()
        capcheck()
        test.append(temp)
        
    if x == 4:
        test.append(" ")
        r_noun()
        capcheck()
        test.append(temp)

        test.append(" ")
        r_verb()
        capcheck()
        test.append(temp)

        test.append(" ")
        r_noun()
        capcheck()
        test.append(temp)

def newsentence():
    global dictionary
    global sentence
    global test
    global first

    test = []

    first = True

    x = random.randint(0, 2)
    y = random.randint(0, len(connectors)-1)

    if x == 0:
        newsentencebase()
        test.append(" ")
        test.append(connectors[y])
        newsentencebase()
        
    if x == 1:
        newsentencebase()
        test.append(", ")
        test.append(connectors[y])
        newsentencebase()
        
    if x == 2:
        newsentencebase()
    

    test.append('.')
    sentence = sentence.join(test)


def newparagraph():
    global sentence
    global paragraph

    new = []

    x = random.randint(25, 50)

    for i in range(1, x):
        newsentence()
        new.append(sentence)
        sentence = ""

    paragraph = paragraph.join(new)

def newtext():
    global paragraph
    global dictionary
    global extra

    for i in range(1, 50):
        newword()

    text = ""
    
    new = []


    for i in range(0, 3):
        newparagraph()
        new.append(paragraph)
        paragraph = ""
        
        new.append('''
        ''')

    
    text = text.join(new)
    print(text)
 
newtext()
