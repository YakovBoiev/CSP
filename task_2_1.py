"""
Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель
системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список.
Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции
создать главный список для хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета
в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также
оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
"""
import re
import csv


def get_data():
    main_data = [['Изготовитель ОС', 'Название ОС', 'Код продукта', 'Тип системы']]
    os_prod_list = []
    os_name_list = []
    os_cod_list = []
    os_type_list = []
    file_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    for file in file_list:
        with open(file, encoding='windows-1251') as f:
            for line in f.readlines():
                line = re.split(':\s*', line)
                if line[0] == main_data[0][0]:
                    os_prod_list.append(line[1].rstrip())
                if line[0] == main_data[0][1]:
                    os_name_list.append(line[1].rstrip())
                if line[0] == main_data[0][2]:
                    os_cod_list.append(line[1].rstrip())
                if line[0] == main_data[0][3]:
                    os_type_list.append(line[1].rstrip())
    os_param_list = [os_prod_list, os_name_list, os_cod_list, os_type_list]
    while len(os_param_list[0]):
        row = []
        for item in os_param_list:
            row.append(item.pop(0))
        main_data.append(row)
    return main_data


def write_to_csv(out_file):
    with open(out_file, 'w', encoding='utf-8', newline='') as f:
        f_writer = csv.writer(f)
        for row in get_data():
            f_writer.writerow(row)


write_to_csv('output_2_1.csv')