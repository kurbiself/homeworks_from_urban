immutable_var = (13, 'Friday', False, [1,3])
print('immutable tuple:', immutable_var)
print('second element of the tuple:', immutable_var[1])
print('first list element of a tuple:',immutable_var[3][0])
# Кортеж является неизменяемым типом данных, поэтому мы не можем заменить элемент в нём:
# immutable_var[0] = 11
mutable_list = [13, 'Friday', False, [1,3]]
print('original list:', mutable_list)
mutable_list[0] = 11
mutable_list.append('sale')
print('modified list:', mutable_list)
