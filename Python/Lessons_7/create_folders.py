#!/usr/bin/env python3


import os


PATH = {
    'my_project': {
        'settings',
        'settings',
        'mainapp',
        'adminapp',
        'authapp'
    }
}


def creating_folders(path):
    try:
        for folder in path:
            for in_folder in path[folder]:
                os.makedirs(f'{os.path.dirname(__file__)}/{folder}/{in_folder}')        
        print('Done')
    except FileExistsError as error:
        print(f'Nothing create, dir exists {error.filename}')

creating_folders(PATH)