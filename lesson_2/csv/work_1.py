# Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
# info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
#
# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными,
# их открытие и считывание данных. В этой функции из считанных данных необходимо с помощью регулярных выражений
# извлечь значения параметров «Изготовитель системы»,  «Название ОС», «Код продукта», «Тип системы».
# Значения каждого параметра поместить в соответствующий список.
# Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
# В этой же функции создать главный список для хранения данных отчета — например, main_data —
# и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта»,
# «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data
# (также для каждого файла);
#
# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение
# данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
# Проверить работу программы через вызов функции write_to_csv().

import csv

os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []

def get_data(*file_names):
    main_data = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    for file_name in file_names:
        with open(file_name, 'r', encoding='utf-8') as f:
            data = f.read().split('\n')
            os_prod_list.append(data[0].replace(main_data[0] + ': ', ''))
            os_name_list.append(data[1].replace(main_data[1] + ': ', ''))
            os_code_list.append(data[2].replace(main_data[2] + ': ', ''))
            os_type_list.append(data[3].replace(main_data[3] + ': ', ''))
    return main_data

def write_to_csv(csv_file_name):
    main_data = get_data('info_1.txt', 'info_2.txt', 'info_3.txt')
    data = [main_data, os_prod_list, os_name_list, os_code_list, os_type_list]
    with open(csv_file_name, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)

write_to_csv('info_result.csv')
