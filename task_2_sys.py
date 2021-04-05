#!/usr/bin/env python3
import sys
from task_2 import chek_list_len

file_name1 = sys.argv[1]
file_name2 = sys.argv[2]
file_name3 = sys.argv[3]

with open(file_name1, 'r', encoding='utf-8') as user_name, \
        open(file_name2, 'r', encoding='utf-8') as user_hobby, \
        open(file_name3, 'w', encoding='utf-8') as f3:
    for el_user in user_name:
        el_hobby = user_hobby.readline().strip()
        if not el_hobby:
            el_hobby = None
        f3.write(f'{el_user.strip()}: {el_hobby}\n')
    chek_list_len(user_name, user_hobby)
    
