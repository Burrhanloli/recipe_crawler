import json
import re
file_name = 'recipe_morrocan_final.json'

values = {
    '\u2009': '',
    '\u00bd': '.5',
    '\u00bc': '.25',
    '\u00be': '.75',
    '\u2154': '.66',
    '\u2155': '.20',
    '\u2156': '.80',
    '\u2153': '.33',
    '\u2157': '.67',
    '\u215b': '.12',
    'to taste': '1',
}

with open(file_name) as f:
    data = json.load(f)

    list = []
    for i in data:
        ingredientList = []
        for j in i['ingredients']:
            quantity = j['quantity']
            # if bool(re.match(r"\(.*?\)", quantity)) == True:

            print(quantity)
            quantity = re.sub(r"\(.*?\)", "", quantity)
            print('changed')
            print(quantity)
            for v in values:
                quantity = quantity.replace(v, values[v])
            if quantity == '':
                quantity = "1"
            j['quantity'] = float(quantity)
            ingredientList.append(j)
        i['ingredients'] = ingredientList
        list.append(i)

    with open(file_name, 'w') as outfile:
        json.dump(list, outfile)
