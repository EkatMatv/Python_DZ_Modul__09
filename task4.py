'''Дан текстовый файл. Найти длину самой длинной
строки.'''

with open('text3.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
length_line = 0
count_line = 1
for i in range(len(lines)):
    if len(lines[i]) > length_line:
        length_line = len(lines[i])
        long_line = lines[i]
        count_line += 1
print(f'\nСАМАЯ ДЛИННАЯ СТРОКА: {long_line}')
print(f'НОМЕР СТРОКИ: {count_line}')
