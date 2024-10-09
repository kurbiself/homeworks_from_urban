from datetime import datetime
from multiprocessing import Pool


def read_info(name: str):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
            # all_data = file.read().rstrip().split('\n')


if __name__ == '__main__':
    start_linear = datetime.now()
    file_name = [f'file {i}.txt' for i in range(1, 5)]
    for f in file_name:
        read_info(f)
    end_linear = datetime.now()
    print('t работы линейного процесса:', end_linear - start_linear)

    start_multiprocessor = datetime.now()
    with Pool(4) as pool:
        pool.map(read_info, file_name)
    end_multiprocessor = datetime.now()
    print('t работы многопроцессорного д-ия:', end_multiprocessor - start_multiprocessor)
