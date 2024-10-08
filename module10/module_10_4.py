from threading import Thread
from queue import Queue
from random import randint
from time import sleep


class Guest(Thread):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def run(self):
        expectation = randint(3, 10)
        sleep(expectation)


class Table:
    def __init__(self, number: int, guest: Guest = None):
        self.number = number
        self.guest = guest


class Cafe:
    def __init__(self, *args):
        self.tables = list(args)
        self.queue = Queue()

    def guest_arrival(self, *guests):
        table_is_free = True
        for new_guest in guests:
            for table in self.tables:
                if table.guest is None:
                    table.guest = new_guest
                    new_guest.start()
                    print(f'{new_guest.name} сел за стол №{table.number}')
                    table_is_free = True
                    break
                else:
                    table_is_free = False
            if not table_is_free:
                self.queue.put(new_guest)
                print(f'{new_guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty():
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла). '
                          f'Стол номер {table.number} свободен')
                    table.guest = None
                if table.guest is None and not self.queue.empty():
                    table.guest = self.queue.get()
                    table.guest.start()
                    print(f"{table.guest.name} вышел(-ла) из очереди "
                          f"и сел(-а) за стол номер {table.number}")


tables = [Table(number) for number in range(1, 6)]
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
