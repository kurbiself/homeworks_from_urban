def calculate_structure_sum(*args):
    result = 0
    for i in args:
        if type(i) == list:
            result += calculate_structure_sum(*i)
        if type(i) == dict:
            for keys, values in i.items():
                result += calculate_structure_sum(keys, values)
        if type(i) == tuple:
            result += calculate_structure_sum(*i)
        if type(i) == set:
            result += calculate_structure_sum(*i)
        if type(i) == int:
            result += i
        if type(i) == str:
            result += len(i)
    return result


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)