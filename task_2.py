#!/usr/bin/env python3


import sys
import json


user_resault = {}

def chek_list_len(list_1, list_2):
    if len(list(list_1)) < len(list(list_2)):
        return sys.exit(1) 


with open(r'./Lessons_6/users.csv', 'r', encoding='utf-8') as user_name, \
    open(r'./Lessons_6/hobby.csv', 'r', encoding='utf-8') as user_hobby:

    for el_user in user_name:
        el_hobby = user_hobby.readline().strip()
        if not el_hobby:
            el_hobby = None
        if el_user not in user_resault:
            user_resault[el_user.strip()] = el_hobby
    chek_list_len(user_name, user_hobby)
    
print(user_resault)
