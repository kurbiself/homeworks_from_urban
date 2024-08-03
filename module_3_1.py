calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string_arg: str) -> tuple:
    count_calls()
    new_tuple = (len(string_arg), string_arg.upper(), string_arg.lower())
    return new_tuple


def is_contains(string_arg: str, list_arg: list) -> bool:
    count_calls()
    result = False
    for i in list_arg:
        if type(i) != str:
            continue
        else:
            if string_arg.lower() == i.lower():
                result = True
    return result


list1 = ['Мне', 4, 'нравится', 'мопс']
str1 = 'мне'
print(is_contains(str1, list1))
string_info(str1)
string_info('Jojo')
print('Количество вызовов функций:', calls)