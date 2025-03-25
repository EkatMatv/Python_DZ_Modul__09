'''Дан текстовый файл. Найти и заменить в нем задан-
ное слово. Что искать и на что заменять определяется
пользователем.'''
import re

import re
with open('text3.txt', 'r', encoding='utf-8') as file:
    text = file.read()

    replace_word = input('Введите слово, которое надо заменить: ')
    my_word = input('Введите слово, на которое надо заменить: ')
    new_text = text.replace(replace_word, my_word)

with open('text3.txt', 'w', encoding='utf-8') as file:
    file.write(new_text)
print(f'\nТекст после замены:\n{new_text}')