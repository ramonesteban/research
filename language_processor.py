import difflib
import re

negativeWords = [
    'terrible',
    'horrible',
    'evil',
    'die',
    'dick',
    'bitch',
    'fucked',
    'stupid',
    'idiot',
    'dumb',
    'noob',
    'shit',
    'vain',
    'n00b',
    'dickhead',
    'cocksucker',
    'disgusting',
    'slut'
]
positiveWords = [
    'happy',
    'good',
    'great',
    'amazing',
    'awesome',
    'wonderful',
    'brilliant',
    'smart'
]
places = [
    'mexico',
    'usa'
]

def is_positive(word):
    for test in positiveWords:
        similarity = difflib.SequenceMatcher(None, test, word).ratio()
        if similarity > 0.8:
            print word + ' is positive word'
            return True

def is_negative(word):
    for test in negativeWords:
        similarity = difflib.SequenceMatcher(None, test, word).ratio()
        if similarity > 0.8:
            print word + 'is negative word'
            return True


def is_place(word):
    for test in places:
        similarity = difflib.SequenceMatcher(None, test, word).ratio()
        if similarity > 0.8:
            print word + ' is a known place'
            return True


def is_hashtag(word):
    p = re.compile('#+\w*')
    match = p.findall(word)
    if len(match) > 0:
        return True

def main():
    fragments = [
        "Nueva Wal-Mart de Mexico",
        "PEPSI-COLA",
        "COCA-COLA",
        "Smart product",
        "Tastes horrible",
        "the 28th of december",
        "the ticket is 212-323-1239",
        "from Mexico",
        "number 1 800 567-4321",
        "costs $23 per person",
        "website http://theevent.com",
        "some comments at #coolevent",
        "David david32@gmail.com"
    ]

    for fragment in fragments:
        words = fragment.split()
        for word in words:
            word = word.lower()
            result = is_positive(word)
            if result == True:
                print 'so <<' + fragment + '>> is a positive text'
                print '****************************'

            result = is_negative(word)
            if result == True:
                print 'so <<' + fragment + '>> is a negative text'
                print '****************************'

            result = is_place(word)
            if result == True:
                print '<<' + fragment + '>> contains a place'
                print '****************************'

            result = is_hashtag(word)
            if result == True:
                print '<<' + fragment + '>> has a hashtag'
                print '****************************'

if __name__ == '__main__':
    main()
