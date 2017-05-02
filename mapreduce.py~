book = ['a','b','b','b','c','d']


def sameWord(w, w2):
    if w == w2:
        return 1
    return 0

def add(a, b):
    return a + b


def freq(word):
    return reduce(add, map(lambda x: sameWord(x, word), book))

print freq('b')
