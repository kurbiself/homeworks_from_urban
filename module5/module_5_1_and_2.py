class House:
    def __init__(self, name: int, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int) -> None:
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f'{new_floor}-ого этажа не существует')
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


barbie_dream_house = House('ЖК Barbie', 3)
#barbie_dream_house.go_to(3)
print(len(barbie_dream_house))
print(barbie_dream_house)