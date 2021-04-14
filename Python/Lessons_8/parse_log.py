#!/usr/bin/env python3


import re
import requests


pattern = re.compile(
    r'([\da-f]{1,4}[.:][\da-f]{1,4}[.:][\da-f]{1,4}[.:][\da-f]{1,4})[^\[]+\[([^\]]+)\]\W+([a-zA-Z]+)([^"]+)\D+(\d+)(\d+)'
    )

def parse_log_nginx(patern):
    with open(r'./Lessons_8/nginx_log.txt', 'r', encoding='utf-8') as log:
        for line in log:
            res = pattern.search(line)
            print(res.groups())

parse_log_nginx(pattern)