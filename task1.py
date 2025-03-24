'''Дано два текстовых файла. Выяснить, совпадают ли
их строки. Если нет, то вывести несовпадающую строку
из каждого файла.'''

file = open('text1.txt', 'r', encoding='utf-8')
lines1 = file.readlines()
file = open('text2.txt', 'r', encoding='utf-8')
lines2 = file.readlines()
max_lines = max(len(lines1), len(lines2))
if lines1 == lines2:
    print('Все строки в файлах совпадают')
for i in range(max_lines):
    line1 = lines1[i] if i < len(lines1) else ' '
    line2 = lines2[i] if i < len(lines2) else ' '
    if line1 != line2:
         print(f"Несовпадение в строке {i + 1}:")
         print(f'Файл 1: {line1}')
         print(f'Файл 2: {line2}')

