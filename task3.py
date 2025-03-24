'''Дан текстовый файл. Удалить из него последнюю
строку. Результат записать в другой файл.'''

with open('text3.txt', 'r', encoding='utf-8') as file:
    text = file.readlines()

if text:
    text = text[:-1]
with open('last_line.txt', 'w', encoding='utf-8') as file:
    file.writelines(text)
