import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        days = 0
        enemies = 100
        print(f'{self.name}, на нас напали!')
        while enemies:
            time.sleep(1)
            days += 1
            enemies -= self.power
            print(f'{self.name} сражается {days} дней, осталось {enemies} войнов.')

        print(f'{self.name} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Gaahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
