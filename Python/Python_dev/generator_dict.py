#!/usr/bin/env python3


list_1 = ["Russia", "Ukraine", "USA", "Canada"]
list_2 = ['Moscow', 'Kiev', 'Washington']

result_list = {}

def dictonory_add(list_1, list_2):
    for el in list_1:
        if len(list_1) > len(list_2):
            list_2.append(None)
            result_list = dict(zip(list_1, list_2))
        else:
            result_list = dict(zip(list_1, list_2))
    return result_list


print(dictonory_add(list_1, list_2))