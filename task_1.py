#!/usr/bin/env python3

import requests


ip_response = []

respons = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
text_res = respons.text


with open(r'./Lessons_6/nginx_logs.txt', 'r+', encoding='utf-8') as f:
    ip_response = [(line.split()[0], line.split()[5].strip('"'), line.split()[6]) for line in f]

# for out in ip_response:
#     print(out)

user_response = []
spam_ip = {}
with open(r'./Lessons_6/nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        ln = line.split()
        ip = ln[0]
        user_response.append((ip, ln[5].strip('"'), ln[6]))
        if ip not in spam_ip:
            spam_ip[ip] = 0
        else:
            spam_ip[ip] += 1

get_index = 0
ip_spam = ''
for key, value in spam_ip.items():
    if value > get_index:
        get_index = value
        ip_spam = key
print('IP спам: ', ip_spam, get_index)
