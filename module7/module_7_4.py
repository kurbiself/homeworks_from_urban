class Team:
    """Класс отображает команду и её достижения.

    Attributes:
        name (str): Название команды.
        team_num (int): Количество участников команды.
        team_time(float): Время, за которое справилась команда.
        score(int): Количество решённых задач.

    """

    def __init__(self, name: str, team_num: int, team_time: float, score: int):
        self.name = name
        self.team_num = team_num
        self.team_time = team_time
        self.score = score

    def __str__(self) -> str:
        """Описание команды.

        Returns:
            Информация, сколько участников в команде с определённым названием.

        """
        return 'В команде %s участников: %s!' % (self.name, self.team_num)

    def result_of_score(self) -> str:
        """Строковое представление результата решения задач.

        Returns:
            Информация о том, сколько задач решила команда.

        """
        return 'Команда {} решила задач: {}!'.format(self.name, self.score)

    def result_of_time(self) -> str:
        """Строковое представление времени, которое опнадобилось для решения задач.
        Returns:
            Информация о о времени.
        """

        return '{} решили задачи за {} c!'.format(self.name, self.team_time)


class Challenge:
    """Класс отображает результаты соревнований двух команд

    Attributes:
        team1 (Team): Первая команда
        team2 (Team): Вторая команда

    """

    def __init__(self, team1: Team, team2: Team):
        self.team1 = team1
        self.team2 = team2

    def numbers_of_members(self) -> str:
        """Строковое представление количества участников команд.
        Returns:
            Информация о количестве участников.
        """
        return 'Итого сегодня в командах участников: %s и %s!' % (self.team1.team_num, self.team2.team_num)

    def results_of_score_and_time(self) -> str:
        """Строковое представление количества и времени решения задач.
        Returns:
            Информация о испытаниях.
        """
        scores = self.team1.score + self.team2.score
        average_time = round((self.team1.team_time + self.team2.team_time) / scores, 2)
        return f'Сегодня было решено {scores} в среднем по {average_time} секунды на задачу!.'

    def challenge_result(self) -> str:
        """Выбор победителя.
        Returns:
            Оглашение результатов и победителя испытаний.
        """
        if (self.team1.score > self.team2.score or self.team1.score == self.team2.score
                and self.team1.team_time > self.team2.team_time):
            result = f'Победа команды {self.team1.name}!'
        elif (self.team1.score < self.team2.score or self.team1.score == self.team2.score
              and self.team1.score < self.team2.score):
            result = f'Победа команды {self.team2.name}!'
        else:
            result = 'Ничья!'
        return result


team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 18015.2
team2_time = 19003.1

code_masters = Team('Мастера кода', team1_num, team1_time, score_1)
data_wizards = Team('Волшебники данных', team2_num, team2_time, score_2)
game = Challenge(code_masters, data_wizards)
print(code_masters.result_of_time())
print(data_wizards.result_of_time())
print(code_masters.result_of_score())
print(data_wizards.result_of_score())
print(game.results_of_score_and_time())
print(game.numbers_of_members())
print(game.challenge_result())
