import inspect


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def voice(self):
        print(f'Привет! Меня зову {self.name}, мне {self.age} лет.')


def introspection_info(obj):
    result_introspection = {'method': [], 'attribute': []}
    for method in dir(obj):
        if callable(getattr(obj, method)):
            result_introspection['method'].append(method)
        else:
            result_introspection['attribute'].append(method)
    result_introspection.update({'type': type(obj)})
    result_introspection.update({'module': inspect.getmodule(obj)})
    return result_introspection


dog = Animal('Sharik', 22)
for k, v in introspection_info(dog).items():
    print(k, v)
