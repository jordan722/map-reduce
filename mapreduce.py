book = ['a','b','b','b','c','d']


def sameWord(w, w2):
    if w == w2:
        return 1
    return 0

def sameWords(w, words):
    if w in words:
        return 1
    return 0

def add(a, b):
    return a + b


def freq(word):
    return reduce(add, map(lambda x: sameWord(x, word), book))

def groupfreq(words):
    return reduce(add, map(lambda x: sameWords(x, words), book))
    

print freq('b')
print groupfreq(['b','c'])
