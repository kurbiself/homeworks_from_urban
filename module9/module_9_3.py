first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) != len(y))
second_result = (True if len(first[x]) == len(second[x]) else False for x in
                 range(len(first) if len(first) < len(second) else len(second)))
print(list(first_result))
print(list(second_result))
