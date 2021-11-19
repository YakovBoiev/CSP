"""
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""

import json


def write_order_to_json(**kwargs):
    order = kwargs
    with open('orders.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    with open('orders.json', 'w', encoding='utf-8') as f:
        data['orders'].append(order)
        json.dump(data, f, indent=4)


write_order_to_json(item=7, quantuty=6, price=8, buyer='geekbrains', data='19.11.2021')
write_order_to_json(item=8, quantuty=10, price=11, buyer='geekbrains', data='19.11.2021')

