def calc(line):
    operand_1, operation, operand_2 = line.split(' ')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    # if operation == '+':
    #     print(f'Result: {operand_1 + operand_2}')
    # if operation == '-':
    #     print(f'Result: {operand_1 - operand_2}')
    # if operation == '/':
    #     print(f'Result: {operand_1 / operand_2}')
    # if operation == '*':
    #     print(f'Result: {operand_1 * operand_2}')
    # if operation == '%':
    #     print(f'Result: {operand_1 % operand_2}')
    # if operation == '//':
    #     print(f'Result: {operand_1 // operand_2}')

cnt = 0

with open('calc.txt', 'r') as file:
    for line in file:
        cnt += 1
        try:
            calc(line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f'Ошибка в линии {cnt}, не хватает данных для выполнения')
            else: #ошибка перевода в число
                print(f'Ошибка в линии {cnt}, нельзя перевести в число')
