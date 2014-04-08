import sys, os
import string
import difflib
import re

brands = [
    'gamesa',
    'minsa',
    '3 estrellas',
    'bimbo',
    'arroz morelos',
    'frijol negro veracruz',
    'valle',
    'fud',
    '1-2-3',
    'gerber',
    'dolores',
    'nescafe',
    'knor suiza',
    'la costena',
    'ibarra',
    'choco choco',
    'dgari',
    'bachoco',
    'nestle',
    'nido',
    'clavel',
    'lala',
    'chipilo',
    'mc cormick',
    'la moderna',
    'la fina',
    'la torre',
    'cloralex',
    'obao',
    'salvo',
    'roma',
    'h-24',
    'zote',
    'palmolive',
    'presto barba',
    'suavelastic',
    'petalo',
    'colgate',
    'duracell',
    'petalo',
    'vanart',
    'pepsi-cola',
    'pepsico',
    'wal-mart'
]

places = [
    'mexico',
    'usa'
]

def is_brand(word):
    for test in brands:
        similarity = difflib.SequenceMatcher(None, test, word).ratio()
        if similarity > 0.8:
            return True

def is_place(word):
    for test in places:
        similarity = difflib.SequenceMatcher(None, test, word).ratio()
        if similarity > 0.8:
            return True

def classifier(text_file_path):
    file_text = open(text_file_path, 'r')
    plain_text = file_text.read()
    plain_text = filter(lambda x: x in string.printable, plain_text)
    words = plain_text.lower().split()
    print plain_text.lower().split()

    product_rate = 0
    brand = False
    place = False

    for word in words:
        result = is_brand(word)
        if result:
            print word + ' is brand word'
            if not brand:
                brand = True
                product_rate += 1

        result = is_place(word)
        if result:
            print word + ' is a known place'
            if not place:
                place = True
                product_rate += 1

    print 'Product rate: %d' % product_rate

def main():
    if len(sys.argv) > 1:
        text_file_path = sys.argv[1]
        if os.path.isfile(text_file_path):
            classifier(text_file_path)
        else:
            print 'Text file does not exist'
    else:
        print 'First parameter must be a text file name'

if __name__ == '__main__':
    main()
