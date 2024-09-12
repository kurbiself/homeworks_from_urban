def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            print('Некорректный тип данных для подсчёта суммы:', number)
            incorrect_data += 1
    new_tuple = (result, incorrect_data)
    return new_tuple


def calculate_average(numbers):
    try:
        result_of_sum = personal_sum(numbers)
        try:
            result = round(result_of_sum[0] / (len(numbers) - result_of_sum[1]), 3)
            return result
        except ZeroDivisionError:
            return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')



print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

