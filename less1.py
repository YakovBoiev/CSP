import subprocess
import chardet


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
        output_list.append(word.encode(encoding='utf-8'))
    return output_list


def byte_str_transform(byte_list):
    output_list = []
    for word in byte_list:
        output_list.append((word.decode(encoding='utf-8')))
    return output_list


def test_ping(*args):
    for site in args:
        subproc_arg = ['ping', '-4', site]
        subprocess_ping = subprocess.Popen(subproc_arg, stdout=subprocess.PIPE)
        for line in subprocess_ping.stdout:
            result = chardet.detect(line)
            line = line.decode(result['encoding']).encode('utf-8')
            print(line.decode('utf-8'))


def create_read_file():
    with open('test_file.txt', 'w') as f:
        f.write('сетевое программирование, сокет, декоратор')
    with open('test_file.txt', 'br') as f:
        result = chardet.detect(f.read())
        print(result['encoding'])
    with open('test_file.txt', 'r', encoding='utf-8', errors='replace') as f:
        for line in f:
            print(line)








type_print('разработка', 'сокет', 'декоратор')
type_print('\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430', '\u0441\u043e\u043a\u0435\u0442',
           '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440')
transform_bite_format('class', 'function', 'method')
print(not_write_byte_type('attribute', 'класс', 'функция', 'type'))
byte_list = str_byte_transform('разработка', 'администрирование', 'protocol', 'standard')
print(byte_list)
print(byte_str_transform(byte_list))
test_ping('www.yandex.ru', 'www.youtube.com')
create_read_file()