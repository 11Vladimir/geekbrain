#!/usr/bin/env python3


import re
import os

patern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

path_log = os.path.abspath(r'./Lessons_8/mail_dump.txt')

def parse_email(path, pattern):
    """
    Find valid e-mail
    
    Function find valid email address and return
    {'username: name, 'domain': domain}
    """
    with open(f'{path}', 'r', encoding='utf-8') as f_mail:
        for el in f_mail.readlines():
            if re.findall(patern, el.strip()):
                print({'username': el.split('@')[0], 'damain': el.split('@')[1].strip()})
            else:
                raise ValueError(f'ValueError: wrong email: {el}')
                    

parse_email(path_log, patern)