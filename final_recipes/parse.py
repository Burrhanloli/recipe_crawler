from collections import namedtuple
import re
import json

import unicodedata as ud
file_name = 'recipe_egyptian_final.json'
print(ud.numeric(u'⅕'))

ASCII_BYTE = " !\"#\$%&\'\(\)\*\+,-\./0123456789:;<=>\?@ABCDEFGHIJKLMNOPQRSTUVWXYZ\[\]\^_`abcdefghijklmnopqrstuvwxyz\{\|\}\\\~\t"


def unicode_strings(buf, n=4):
    reg = b"((?:[%s]\x00){%d,})" % (ASCII_BYTE, n)
    uni_re = re.compile(reg)
    for match in uni_re.finditer(buf):
        try:
            yield match.group().decode("utf-16"), match.start()
        except UnicodeDecodeError:
            pass


with open(file_name) as f:
    data = json.load(f)

    list = []
    for i in data:
        ingredientList = []
        for j in i['ingredients']:
            quantity = j['quantity']
            quantity = unicode_strings(quantity)
            print(quantity)
            j['quantity'] = quantity
            ingredientList.append(j)
        i['ingredients'] = ingredientList
        list.append(i)

    with open('recipe_egyptian_final_test.json', 'w') as outfile:
        json.dump(list, outfile)
