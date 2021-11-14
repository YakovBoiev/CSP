def type_print():
    text = 'разработка', 'сокет', 'декоратор'
    for word in text:
        print(type(word), word)

    text = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430', '\u0441\u043e\u043a\u0435\u0442', \
           '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
    for word in text:
        print(type(word), word)


def transform_bite_format(*args):
    output_data = []
    for word in args:
        b_word = eval(f'b"{word}"')
        print(type(b_word), b_word, len(b_word))


# type_print()
transform_bite_format('class', 'function', 'method')

