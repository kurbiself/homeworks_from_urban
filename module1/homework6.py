#Работа со словарями
my_dict = {'Albert Einstein': 1879, 'Frida Kahlo':1907, 'Karl Marx':1818}
print('my dictionary:', my_dict)
print('existing key:', my_dict['Frida Kahlo'])
print('non-existent key:',my_dict.get('Lenin'))
my_dict.update({'Maya Plisetskaya':1925,
                'Stan Lee': 1922})
print('deleted value:', my_dict.get('Karl Marx'))
del my_dict['Karl Marx']
print('modified dictionary:', my_dict)
#Работа со множествами
my_set = {1,3,3,(1,2,3), '1','1'}
print('original set:',my_set)
my_set.add(2)
my_set.add(978)
my_set.discard((1,2,3))
print('modified set:', my_set)
