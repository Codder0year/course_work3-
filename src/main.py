import json
import os
from datetime import datetime as dt
from config import ROOT_DIR
load_json = os.path.join(ROOT_DIR, "operation.json")
def enterpretated_json(load_json):
    '''
    Загружает данные из JSON файла.
    :return: Список словарей с данными операций
    '''
    with open(load_json) as f:
        list_apres_json = json.load(f)
        return list_apres_json


list_main = enterpretated_json(load_json)


def operations_executed(list_1):
    '''
     выводим операции  executed
    :param list_1: list_apres_json
    :return:list_executed_operations
    '''
    list_executed_operations = []
    for i in list_1:
        if i.get('state') == 'EXECUTED':
            list_executed_operations.append(i)
    return list_executed_operations
list_get_executed = operations_executed(list_main)


def operation_date_filtre(list_2):
    '''
    сортируем по дате
    :param list_2:
    :return:
    '''
    string_date = sorted(list_2, key=lambda x: x['date'], reverse=True)
    return string_date
list_final = operation_date_filtre(list_get_executed)[:5]


def operations_from(list_3):
    '''
    Определяет информацию об отправителе операции.
    :param list_3: Операция из списка выполненных операций
    :return: Информация об отправителе операции
    '''
    variable = list_3.get('from')
    if variable:
        line_from = variable.split(" ")
        part_from = line_from[-1]
        name_card = line_from[:-1]
        if len(part_from) == 16:
            return f"{''.join(name_card)} {part_from[:4]} {part_from[4:6]} {'*' * 2} {'*' * 4} {part_from[-4:]}"
        else:
            return f" {'*' * 2} {part_from[-4:]}"
    else:
        return "Инкогнито"  # Возвращаем пустую строку, если отправитель не указан


def operations_to(list_3):
    '''
    Определяет информацию о получателе операции.
    :param list_3: Операция из списка выполненных операций
    :return: Информация о получателе операции
    '''
    variable = list_3.get('to')
    if variable:
        line_to = variable.split(" ")
        part_to = line_to[-1]
        name_card = line_to[:-1]
        if len(part_to) == 16:
            return f"{''.join(name_card)} {part_to[:4]} {part_to[4:6]} {'*' * 2} {'*' * 4} {part_to[-4:]}"
        else:
            return f"Счет: {'*' * 2} {part_to[-4:]}"


def operation_data(list_3):
    '''
    Форматирует дату операции в формат "день.месяц.год".
    :param list_3: Операция из списка выполненных операций
    :return: Отформатированная дата операции
    '''
    variable = list_3["date"]
    filter_data = dt.strptime(variable, '%Y-%m-%dT%H:%M:%S.%f')
    return filter_data.strftime('%d.%m.%Y')


def operation_description(list_3):
    '''
    Определяет описание операции.
    :param list_3: Операция из списка выполненных операций
    :return: Описание операции
    '''
    variable = list_3.get('description')
    return variable


for i in list_final:
    data_stdout = operation_data(i)
    description_stdout = operation_description(i)
    print(f"{data_stdout} {description_stdout}")
    variable_from = operations_from(i)
    variable_to = operations_to(i)
    print(f"{variable_from} -> {variable_to}")
    print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")
    print()