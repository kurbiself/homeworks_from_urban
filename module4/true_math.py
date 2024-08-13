from math import inf
def divide(first, second: int):
    if second == 0:
        result = inf
    else:
        result = round(first/second, 2)
    return result