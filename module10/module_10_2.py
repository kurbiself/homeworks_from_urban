from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        count_enemy = 100
        count_day = 0
        while count_enemy > 0:
            count_enemy -= self.power
            sleep(1)
            count_day += 1
            if count_enemy < 0:
                count_enemy = 0
            print(f'{self.name} сражается {count_day} день(дня), осталось {count_enemy} воинов.')
        print(f'{self.name} одержал победу спустя {count_day} дней(дня)!')


threads = []

first_knight = Knight('Artas', 20)
second_knight = Knight('Uter', 10)
first_knight.start()
second_knight.start()
threads.append(first_knight)
threads.append(second_knight)
for thread in threads:
    thread.join()
