from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, sides: list, color: list, filled: bool = True):
        if self.__is_valid_color(*color):
            self.__color = color
        else:
            self.__color = [0, 0, 0]
        if self.__is_valid_sides(*sides):
            self.__sides = sides
        else:
            self.__sides = [1] * self.sides_count
        self.filed = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r: int, g: int, b: int) -> bool:
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r: int, g: int, b: int):
        if self.__is_valid_color(r, g, b):
            self.__color[0] = r
            self.__color[1] = g
            self.__color[2] = b

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *sides):
        sides_correct = True
        if len(sides) == self.sides_count:
            for i in sides:
                if not isinstance(i, int) or i < 0:
                    sides_correct = False
                    break
        else:
            sides_correct = False
        return sides_correct

    def __len__(self):
        result = 0
        for side in self.__sides:
            result += side
        return result

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, sides: list, color: list, filled: bool = True):
        super().__init__(sides, color, filled)

    def __radius(self):
        radius = self.get_sides()[0] / 2 * pi  # C/2П
        return radius

    def get_square(self):
        square = 2 * pi * self.__radius() ** 2
        return square


class Triangle(Figure):
    sides_count = 3

    def __init__(self, sides: list, color: list, filled: bool = True):
        super().__init__(sides, color, filled)

    def get_square(self):
        my_sides = self.get_sides()
        half_perimeter = (sum(my_sides)) / 2
        square = sqrt(half_perimeter * (half_perimeter - my_sides[0])
                      * (half_perimeter - my_sides[1])
                      * (half_perimeter - my_sides[2]))
        return square


class Cube(Figure):
    sides_count = 12

    def __init__(self, sides: list, color: list, filled: bool = True):
        if len(sides) == 1:
            self.sides = sides * self.sides_count
        super().__init__(self.sides, color, filled)

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            new_sides = new_sides * 12
        super().set_sides(*new_sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle([10], [200, 200, 100])
cube1 = Cube([6], [222, 35, 130])

circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())
