class Horse:
    def __init__(self, x_distance=0, y_distance=0):
        self.x_distance = x_distance
        self.sound = "Frrr"
        super().__init__(y_distance)

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self, y_distance=0):
        self.y_distance = y_distance
        self.sound = "I train, eat, sleep, and repeat"

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self, x_distance=0, y_distance=0):
        super().__init__(x_distance, y_distance)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return tuple([self.x_distance, self.y_distance])

    def voice(self):
        print(self.sound)


Rainbow_Dash = Pegasus()

print(Rainbow_Dash.get_pos())
Rainbow_Dash.move(10, 15)
print(Rainbow_Dash.get_pos())
Rainbow_Dash.move(-5, 20)
print(Rainbow_Dash.get_pos())

Rainbow_Dash.voice()
