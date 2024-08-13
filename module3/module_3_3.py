def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
values_list = [['first', 'second'], (1, 2), 3]
values_dict = {
    'a': False,
    'b': 'second',
    'c': 3
}
print_params(*values_list)
print_params(**values_dict)
values_list2 = [1,'two']
print_params(*values_list2, 42)
