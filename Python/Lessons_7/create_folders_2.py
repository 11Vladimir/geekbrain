#!/usr/bin/env python3

import os


def create_parent(dir_name):
    try:
        os.mkdir(dir_name)
    except FileExistsError as e:
        print(f'dir exists: {e.filename}')
    return 0


def create_child_dirs(parent, *dirs):
    for el in dirs:
        try:
            dir_path = os.path.join(parent, el)
            os.mkdir(dir_path)
        except FileExistsError as e:
            print(f'dir exists: {e.filename}')
        return 0


def create_starter(main_dir):
    create_parent(main_dir)
    create_child_dirs('settings', 'mainapp', 'adminapp', 'authapp')