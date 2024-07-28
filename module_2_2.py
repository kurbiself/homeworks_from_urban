first = input('Enter first number: ')
second = input('Enter second number: ')
third = input('Enter third  number: ')
if first == second and second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)