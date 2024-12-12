import time
import multiprocessing as mp

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)
    # print(f'Завершилось чтение из файла {name}')

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейное выполнение
start_time = time.time()
for filename in filenames:
    read_info(filename)
linear_time = time.time() - start_time
print(f'Линейное выполнение: {linear_time}')

# Многопроцессное выполнение
# if __name__ == '__main__':
#     start_time = time.time()
#     with mp.Pool(processes=4) as pool:
#         pool.map(read_info, filenames)
#     multiprocess_time = time.time() - start_time
#     print(f'Многопроцессное выполнение: {multiprocess_time}')
