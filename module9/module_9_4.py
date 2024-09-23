import random

# лямбда функция
first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda x, y: x == y, first, second))
print(result)


# замыкание
def get_advanced_writer(file_name):
    file_n = file_name

    def write_everything(*data_set):
        with open(file_n, 'a', encoding='utf-8') as file:
            for line in data_set:
                print(line)
                file.write(str(line) + '\n')

    return write_everything


class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
