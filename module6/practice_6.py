import arcade

screen_width = 800
screen_height = 600
screen_title = 'Pong Game'


class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('bar.png', 0.4)

    def update(self):
        self.center_x += self.change_x
        if self.right >= screen_width:
            self.change_x = -self.change_x
        elif self.left <= 0:
            self.change_x = -self.change_x


class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('ball.png', 0.2)
        self.change_x = 5
        self.change_y = 5

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= screen_width:
            self.change_x = -self.change_x
        elif self.left <= 0:
            self.change_x = -self.change_x
        elif self.top >= screen_height:
            self.change_y = -self.change_y
        elif self.bottom <= 0:
            self.change_y = -self.change_y


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bar = Bar()
        self.ball = Ball()
        self.setup()

    def setup(self):
        self.bar.center_x = screen_width / 2
        self.bar.center_y = screen_height / 5
        self.ball.center_x = screen_width / 2
        self.ball.center_y = screen_height / 2

    def on_draw(self):
        self.clear((255, 255, 255))
        self.bar.draw()
        self.ball.draw()

    def update(self, delta):
        if arcade.check_for_collision(self.bar, self.ball):
            self.ball.change_y = -self.ball.change_y
        self.ball.update()
        self.bar.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.bar.change_x = 5
        if key == arcade.key.LEFT:
            self.bar.change_x = -5

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.bar.change_x = 0


if __name__ == '__main__':
    window = Game(screen_width, screen_height, screen_title)
    arcade.run()
