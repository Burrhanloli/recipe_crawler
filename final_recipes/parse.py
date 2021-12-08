import json

import fractions
import quopri
import unicodedata as ud
file_name = 'recipe_egyptian_final.json'
ud.numeric(u'⅕')
with open(file_name) as f:
    data = json.load(f)

    list = []
    for i in data:
        ingredientList = []
        for j in i['ingredients']:
            quantity = j['quantity']
            print(quantity)
            if '\\u' in quantity:
                string_ = quopri.decodestring(quantity).decode('utf-8')
                # Assume each string is composed solely of one or more digits,
                # with the fraction character at the end
                int_part = int(string_[:-1])

                normalised = ud.normalize('NFKD', string_[-1])
                # Note that the separator character here is chr(8260),
                # the 'FRACTION SLASH' character, not the ASCII 'SOLIDUS'
                nominator, _, denominator = normalised.partition('⁄')

                fractional_part = fractions.Fraction(
                    *map(int, (nominator, denominator)))

                print(
                    f'Integer part {int_part}, fractional part {fractional_part!r}')
            j['quantity'] = quantity
            ingredientList.append(j)
        i['ingredients'] = ingredientList
        list.append(i)

    with open('recipe_egyptian_final_test.json', 'w') as outfile:
        json.dump(list, outfile)
