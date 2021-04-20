#!/usr/bin/env python3


list_1 = ["Russia", "Ukraine", "USA"]
list_2 = ['Moscow', 'Kiev']

result_list = {}


for el in list_1:
    if len(list_1) > len(list_2):
        result_list = dict(zip(list_1, list_2))


print(result_list)