from time import sleep
from typing import Optional


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'Пользователь "{self.nickname}"'

    def __repr__(self):
        return f'nickname = {self.nickname}, password = {self.password}, age = {self.age}'


class UrTube:
    users = []
    videos = []
    current_user: Optional[User] = None

    def __repr__(self):
        return f'users = {self.users},videos = {self.videos}, current_user = {self.current_user}'

    def log_in(self, nickname: int, password: int):
        previous_user = self.current_user

        for i in self.users:
            if i.nickname == nickname and i.password == hash(password):
                self.current_user = i
                break

        if previous_user == self.current_user:
            print('Неверный логин или пароль')

    def register(self, nickname: str, password: str, age: int):
        is_exist = False
        for user in self.users:
            if nickname.lower() == user.nickname.lower():
                is_exist = True
                break
        if not is_exist:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user
        else:
            print('Пользователь с таким именем уже существует!')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for new_video in args:
            is_exist = False
            for video in self.videos:
                if new_video.title == video.title:
                    is_exist = True
            if is_exist:
                break
            self.videos.append(new_video)

    def get_videos(self, search_word: str) -> list:
        search_list = []
        for i in self.videos:
            if search_word.lower() in i.title.lower():
                search_list.append(i.title)
        return search_list

    def watch_video(self, title_video):
        if self.current_user == None:
            print('Войдите в акканут для просмотра видео')
        else:
            for i in self.videos:
                if title_video == i.title:
                    if i.adult_mode and self.current_user.age >= 18 or not i.adult_mode:
                        print(f'Просмотр фильма на {i.time_now}')
                        for t in range(i.time_now, i.duration + 1):
                            print(t)
                            sleep(1)
                        i.time_now = None
                        print('Конец видео')
                    else:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    break


class Video:
    def __init__(self, title: str, duration: int, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'Видео {self.title} длительностью {self.duration}'

    def __repr__(self):
        return f'title = {self.title}, duration = {self.duration}, time_now = {self.time_now}, adult_mode = {self.adult_mode}'


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
