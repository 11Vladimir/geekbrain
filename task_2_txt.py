#!/usr/bin/env python3
import sys


with open(r'./Lessons_6/users.csv', 'r', encoding='utf-8') as user_name, \
        open(r'./Lessons_6/hobby.csv', 'r', encoding='utf-8') as user_hobby, \
        open('./Lessons_6/users_hobby.txt', 'w', encoding='utf-8') as f3:
    for el_user in user_name:
        el_hobby = user_hobby.readline().strip()
        if not el_hobby:
            el_hobby = None
        f3.write(f'{el_user.strip()}: {el_hobby}\n')
    content = user_hobby.readline()
    if content:
        sys.exit(1)
