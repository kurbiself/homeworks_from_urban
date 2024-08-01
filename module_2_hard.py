def password(first_number: int) -> str:
    flag = set()
    flag2 = set()
    result = ''
    for i in range(1, first_number):
        for j in range(1, first_number):
            if i in flag and j in flag2:
                continue
            if first_number % (i + j) == 0 and i != j:
                result = result + str(i) + str(j)
                flag.add(j)
        flag2.add(i)
    return result


input_number = int(input('Число первой вставки от 3-20:'))
print(password(input_number))
