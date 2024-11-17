import threading
import time


def write_words(word_count, file_name):
    for i in range(word_count):
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f'Какое-то слово №{i + 1} \n')
            time.sleep(0.1)

    print(f'Завершилась запись в файл {file_name}')


start_func = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_func = time.time()

print(f'Работа функций завершилась за {round(end_func - start_func, 2)}')

start_thr = time.time()
tr1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
tr2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
tr3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
tr4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

tr1.start()
tr2.start()
tr3.start()
tr4.start()

tr1.join()
tr2.join()
tr3.join()
tr4.join()
end_thr = time.time()

print(f'Работа потоков завершилась за {round(end_thr - start_thr, 2)}')