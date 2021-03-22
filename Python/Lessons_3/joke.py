"""
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого)
"""


import random


def get_jokes(count_j):
    nouns = ["автомобиль", "лес.", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    joke = []
    for i in range(count_j):
        joke.append(f"{nouns[random.randint(0,4)]} {adverbs[random.randint(0,4)]} {adjectives[random.randint(0,4)]}")
    return joke


count = int(input("Введите желаемое число шуток:\n"))

print(f"Созданые шутки:\n {get_jokes(count)}")

print()