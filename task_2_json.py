#!/usr/bin/env python3

import sys
import json

result_dict = {}
with open(r'./Lessons_6/users.csv', 'r', encoding='utf-8') as user_name, \
        open(r'./Lessons_6/hobby.csv', 'r', encoding='utf-8') as user_hobby:

    users_name = (el for el in user_name.read().splitlines())
    hobbies_data = (el for el in user_hobby.read().splitlines())

    for hobbies, user in zip(hobbies_data, users_name):
        result_dict[user.strip()] = hobbies.strip()
    for _ in hobbies_data:
        sys.exit(1)
    for user in users_name:
        result_dict[user.strip()] = None

print(result_dict)

with open('./Lessons_6/result.json', 'w', encoding='utf-8') as result_file:
    json.dump(result_dict, result_file, ensure_ascii=False)
