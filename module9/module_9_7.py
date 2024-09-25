def is_prime(func):
    def wrapper(*args):
        number = func(*args)
        flag = True
        if number == 1:
            flag = False
        else:
            for i in range(2, number):
                if number % i == 0:
                    flag = False
                    break
        if flag:
            return f'{number} - проcтое'
        else:
            return f'{number} - составное'

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(120, 1, 2)
print(result)
