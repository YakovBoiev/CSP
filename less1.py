def type_print(*args):
    for word in args:
        print(type(word), word)


def transform_bite_format(*args):
    for word in args:
        b_word = eval(f'b"{word}"')
        print(type(b_word), b_word, len(b_word))


def not_write_byte_type(*args):
    output_list = []
    for word in args:
        for char in word:
            if ord(char) > 255:
                output_list.append(word)
                break
    return output_list


def str_byte_transform(*args):
    output_list = []
    for word in args:
        output_list.append(word.encode('utf-8'))
    return output_list


def byte_str_transform(byte_list):
    output_list = []
    for word in byte_list:
        output_list.append((word.decode('utf-8')))
    return output_list


type_print('разработка', 'сокет', 'декоратор')
type_print('\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430', '\u0441\u043e\u043a\u0435\u0442',
           '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440')
transform_bite_format('class', 'function', 'method')
print(not_write_byte_type('attribute', 'класс', 'функция', 'type'))
byte_list = str_byte_transform('разработка', 'администрирование', 'protocol', 'standard')
print(byte_list)
print(byte_str_transform(byte_list))
