class Database:
    def __init__(self):
        self.data = {}

    def add_usr(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя, содержищий атрибуты: логин, пароль
    """

    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

    @staticmethod
    def valid_password(password: str) -> bool:
        """  Проверка на то, чтобы пароль состоял не менее из 8 символов: букв или цифр.
        Хотя бы один из символов должен быть в верхнем регистре.
        Допустимы следующие символы ['#', '!', '=', '$', '%', '@', '~', '-', '_']

        Args:
            password: принимаемый пароль

        Returns: bool

        """
        simbols = ['#', '!', '=', '$', '%', '@', '~', '-', '_']
        upper_case = False  # флаг на регистр
        password_component = set(password)
        for i in password:
            if i in simbols:
                password_component.discard(i)
            if i.isupper():
                upper_case = True
        password_component = ''.join(password_component)

        if len(password) < 8:
            return False
        elif password_component.isalnum() and upper_case:
            return True
        else:
            return False

if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input('Здравствуйте, пользователь! Выберите следующие дествия: \n1 - Вход \n2 - Регистрация\n'))
        print(choice)
        if choice == 1:
            login = input('Введите логин:')
            password = input('Введите пароль:')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Добро пожаловать, {login}!')
                else:
                    print('Неверный пароль.')
            else:
                print('Пользователь не найден.')
        if choice == 2:
            user = User(input("Введите логин:"), password1 := input("Введите пароль:"),
                    password2 :=input( "Повторите пароль:"))
            if password1 != password2:
                print('Пароль не совпадают, попробуйте ещё раз!')
                continue
            database.add_usr(user.username, user.password)
