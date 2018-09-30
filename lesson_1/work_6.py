# Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
# Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.

import chardet

with open('test_file.txt', 'rb') as f:
    coding = chardet.detect(f.read())
    print(coding['encoding'])

with open('test_file.txt', 'r', encoding='utf-8') as f:
    print(f.read())