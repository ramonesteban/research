import sys, os
import string
import difflib
import re

brands = {
    'gamesa': 0.9,
    'minsa': 0.6,
    '3 estrellas': 0.85,
    'bimbo': 0.9,
    'arroz morelos': 0.8,
    'frijol negro veracruz': 0.8,
    'valle': 0.85,
    'fud': 0.85,
    '1-2-3': 0.9,
    'gerber': 0.9,
    'dolores': 0.9,
    'nescafe': 0.9,
    'knor suiza': 0.8,
    'la costena': 0.8,
    'ibarra': 0.7,
    'choco choco': 0.9,
    'dgari': 0.7,
    'bachoco': 0.8,
    'nestle': 0.9,
    'nido': 0.9,
    'clavel': 0.7,
    'lala': 0.9,
    'chipilo': 0.7,
    'mc cormick': 0.8,
    'la moderna': 0.7,
    'la fina': 0.8,
    'la torre': 0.7,
    'cloralex': 0.9,
    'obao': 0.85,
    'salvo': 0.85,
    'roma': 0.7,
    'h-24': 0.6,
    'zote': 0.7,
    'palmolive': 0.7,
    'presto barba': 0.6,
    'suavelastic': 0.7,
    'petalo': 0.7,
    'colgate': 0.8,
    'duracell': 0.6,
    'petalo': 0.7,
    'vanart': 0.8,
    'pepsi-cola': 0.8,
    'pepsico': 0.8,
    'wal-mart': 0.7
}

places = {
    'mexico': 0.9,
    'usa': 0.6
}

def is_brand(word):
    for brand, value in brands.iteritems():
        similarity = difflib.SequenceMatcher(None, brand, word).ratio()
        if similarity > 0.8:
            return value

def is_place(word):
    for place, value in places.iteritems():
        similarity = difflib.SequenceMatcher(None, place, word).ratio()
        if similarity > 0.8:
            return value

def classifier(text_file_path):
    file_text = open(text_file_path, 'r')
    plain_text = file_text.read()
    plain_text = filter(lambda x: x in string.printable, plain_text)
    words = plain_text.lower().split()
    print plain_text.lower().split()

    product_rate = 0.0
    brand = False
    place = False

    for word in words:
        value = is_brand(word)
        if value != None:
            print word + ' is brand word'
            if not brand:
                brand = True
                product_rate += value

        value = is_place(word)
        if value != None:
            print word + ' is a known place'
            if not place:
                place = True
                product_rate += value

    print 'Product rate: %0.2f' % (product_rate/2.0)

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
