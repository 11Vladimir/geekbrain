"""
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
"""



def num_translate(word):
    english_word = ['zero', 'one', 'two', 'tree', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    russian_word = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    translate_word = ""
    id = 0
    for i in english_word:
        if i == word:
            translate_word = russian_word[id]
        else:
            id -= 1
        id += 1
    # в задании не сказано что необходим обратный перевод, но на всякий случай оставлю код для этого
    # for i in russian_word:
        # if i == word:
            # translate_word = english_word[id]
        # else:
            # id -= 1
        # id += 1
        if id == 0:
            translate_word = None
    return translate_word


word = str(input('Введите число от 0 до 9 для перевода:\n'))

print(f"Перевод вашего слова: {num_translate(word)}")