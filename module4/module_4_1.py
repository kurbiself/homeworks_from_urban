from .fake_math import divide as fake_divide
from . import true_math

print(fake_divide(69,3))
print(fake_divide(3,0))
print(true_math.divide(49, 7))
print(true_math.divide(15, 0))