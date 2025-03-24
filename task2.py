'''Дан текстовый файл. Необходимо создать новый файл
и записать в него следующую статистику по исходному
файлу:
■ Количество символов;
■ Количество строк;
■ Количество гласных букв;
■ Количество согласных букв;
■ Количество цифр.'''

with open('text1.txt', 'r', encoding='utf-8') as file:
    text = file.read()
vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZбвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
digits = "0123456789"
digit_count = 0
vowel_count = 0
consonant_count = 0
for char in text:
    if char in vowels:
        vowel_count += 1
    elif char in consonants:
        consonant_count +=1
    elif char in digits:
        digit_count += 1
total_chars = len(text)
total_lines = text.count('\n') + 1

with open('statistics.txt', 'w', encoding='utf-8') as file:
    file.write(f"Количество символов: {total_chars}\n")
    file.write(f"Количество строк: {total_lines}\n")
    file.write(f"Количество гласных букв: {vowel_count}\n")
    file.write(f"Количество согласных букв: {consonant_count}\n")
    file.write(f"Количество цифр: {digit_count}\n")
print(f"Статистика записана в файл statistics.txt")