import json


def check_value(value, index):
    if len(value) > index and value[index]:
        newStr = value[index].replace('#', '')
        return str(newStr).replace(',', '').strip()
    else:
        return ''


with open("recipe_egyptian.json") as f:
    data = json.load(f)

    list = []
    for i in data:
        ingredientList = []
        for j in i['ingredients']:
            ingredientObj = {}
            splitStr = j.strip().split('#')
            print(splitStr)
            ingredientObj['quantity'] = check_value(splitStr, 1)
            ingredientObj['measurement'] = check_value(splitStr, 2)
            ingredientObj['ingredient'] = check_value(splitStr, 3)
            ingredientObj['comment'] = check_value(splitStr, 4)
            ingredientList.append(ingredientObj)
        i['ingredients'] = ingredientList
        list.append(i)

    print(list)
    with open('recipe_egyptian_final.json', 'w') as outfile:
        json.dump(list, outfile)
