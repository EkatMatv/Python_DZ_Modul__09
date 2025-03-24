'''Дан текстовый файл. Посчитать сколько раз в нем
встречается заданное пользователем слово.'''
import re
with open('text3.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    words = re.split(r'[-,. ]+', content)
    myword = input('Введите слово: ')
    count = 0
    for i in range(len(words)):
        if words[i].upper() == myword.upper():
            count += 1
    print(f'Ваше слово {myword} встречается {count} раз')
