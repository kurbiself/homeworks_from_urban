def divide(first, second: int) -> str:
    if second == 0:
        result = 'Ошибка, на ноль делить нельзя!'
    else:
        result = round(first/second, 2)
    return result
