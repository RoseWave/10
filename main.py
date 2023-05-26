def pr1():
    import json
    with open('1.json', encoding='utf=8') as f:
        templates = json.load(f)
    print(templates)
    for x, y in templates.items():
        print(y)
    for i in y:

        for j in i:
            if j == 'name':
                p = i.get(j)
                j = 'Название:'

            if j == 'price':
                p = i.get(j)
                j = 'Цена:'

            if j == 'weight':
                p = i.get(j)
                j = 'Вес:'

            if j == 'available':
                if i['available'] == True:
                    j = 'В наличии'
                else:
                    j = 'Не в наличии'
                print(j)
            else:
                print(j, p)

        print('\n')

def pr2():
    import json
    with open('1.json', encoding='utf=8') as f:
        templates = json.load(f)
    print(templates)
    for x, y in templates.items():
        print()
    for i in y:
        n = input('Введите название:')
        c = input('Введите цену:')
        v = input('Введите вес:')
        print('\n')

        for j in i:
            if j == 'name':
                i[j] = n
                p = i[j]
                j = 'Название:'

            if j == 'price':
                i[j] = c
                p = i[j]
                j = 'Цена:'

            if j == 'weight':
                i[j] = v
                p = i[j]
                j = 'Вес:'

            if j == 'available':
                if i['available'] == True:
                    j = 'В наличии'
                else:
                    j = 'Не в наличии'
                print(j)
            else:
                print(j, p)

        print('\n')






def pr3():
    with open('ru-en.txt', 'w') as file1:
        with open("en-ru.txt", encoding='utf=8') as file:
            for line in file:
                en = line.split("-")[0].strip()
                ru = line.split("-")[1].strip()
                file1.writelines(f"{ru} - {en}\n")




pr3()