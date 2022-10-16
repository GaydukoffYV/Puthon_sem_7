def view_data(data, title):
    print(f'{title} = {data}')


def get_value():
    return input()


def input_data():
    print('Введите 1 для работы с комплексными числами, 2 - для работы с рациональными числами')
    data_type = get_value()
    if data_type == '1':
        print('Введите первое число (используйте формат: "7 + 4j"):')
        one_value = get_value()
        print('Введите второе число (используйте формат: "7 + 4j"):')
        tue_value = get_value()
        print('Выберите операцию:')
        oper = get_value()
    elif data_type == '2':
        print('Введите первое число (используйте формат: "4/7"):')
        one_value = get_value()
        print('Введите второе число (используйте формат: "4/7"):')
        tue_value = get_value()
        print('Выберите операцию:')
        oper = get_value()
    return (data_type, one_value, oper, tue_value)