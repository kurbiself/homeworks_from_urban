from threading import Thread, Lock
from time import sleep
from random import randint


class Bank:
    balance = 0
    lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            replenishment = randint(50, 500)
            self.balance += replenishment
            print(f'Пополнение: {replenishment}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            cash = randint(50, 500)
            print(f'Запрос на {cash}')
            if cash <= self.balance:
                self.balance -= cash
                print(f'Снятие: {cash}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
