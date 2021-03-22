"""
Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
"""


def thesaurus(names):
    thesaur = {}
    name = []
    id = -1
    for i in range(len(names)):
        for symbol in names[i]:
            if symbol in thesaur:
                for id_1 in range(len(names)):
                    if names[id_1].startswith(symbol):
                        break
                name[id_1 - 1].append(names[i])
                thesaur.setdefault(symbol, name[id_1])
                break
            else:
                id += 1
                name.append([])
                name[id].append(names[i])
                thesaur.setdefault(symbol, name[id])
                break
    return thesaur

names = str(input("Введите список имен через пробел для составления словаря:\n"))
names_list = names.split(' ')

print(names_list)
print(f"Словарь имен: {thesaurus(names_list)}")