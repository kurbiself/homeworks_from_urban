first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(f) for f in first_strings if len(f) >= 5]
second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]
third_result = {x: len(x) for x in first_strings + second_strings if not len(x) % 2}
print(first_result)
print(second_result)
print(third_result)
