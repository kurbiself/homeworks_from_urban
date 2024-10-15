import multiprocessing as mp
from PIL import Image
from queue import Empty


def resize_image(image_paths, pipe: mp.Pipe, stop_event):
    for image_path in image_paths:
        image = Image.open(image_path)
        image = image.resize((100, 100))
        image.save(image_path)
        pipe.send(image_path)  # pipe.put((image_path, image)) - для queve
    stop_event.set()


def change_color(pipe: mp.Pipe, stop_event):
    while not stop_event.is_set():
        try:
            image_path = pipe.recv()
        except Empty:
            break
        image = Image.open(image_path)
        image = image.convert('L')
        image.save(image_path)


if __name__ == '__main__':
    data = []
    # queue = mp.Queue()
    #
    # for image in range(1, 3):
    #     data.append(f'./images/img_{image}.jpg')
    #     print(data)
    #
    # resize_process = mp.Process(target=resize_image, args=(data, queue))
    # change_process = mp.Process(target=change_color, args=(queue, ))
    # resize_process.start()
    # change_process.start()
    # resize_process.join()
    # change_process.join()

    conn1, conn2 = mp.Pipe()
    stop_event = mp.Event()

    for image in range(1, 3):
        data.append(f'./images/img_{image}.jpg')
        print(data)

    resize_process = mp.Process(target=resize_image, args=(data, conn1, stop_event))
    change_process = mp.Process(target=change_color, args=(conn2, stop_event))
    resize_process.start()
    change_process.start()
    resize_process.join()
    change_process.join()
