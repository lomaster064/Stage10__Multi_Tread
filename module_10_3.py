import threading
import time
import random

lock = threading.Lock()

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()


    def deposit(self):
        for i in range(100):
            value = random.randrange(50, 500)

            self.balance += value
            print(f'Пополнение: {value}. Баланс: {self.balance}')
            time.sleep(0.1)

            if self.balance >= 500 and lock.locked():
                lock.release()



    def take(self):
        for i in range(100):
            value = random.randrange(50, 500)
            print(f'Запрос на {value}')

            if value > self.balance:
                print('Запрос отклонен, недостаточно средств')
                lock.acquire()
            else:
                self.balance -= value
                print(f'Снятие: {value}. Баланс: {self.balance}')
                time.sleep(0.1)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')