index = 1


def custom_write(file_name: str, strings: list):
    strings_positions = {}
    with open(file_name, 'a+', encoding="utf-8") as file:
        global index
        for s in strings:
            strings_positions[(index, file.tell())] = s
            file.write(s + '\n')
            index += 1
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test_file.txt', info)
for elem in result.items():
    print(elem)
