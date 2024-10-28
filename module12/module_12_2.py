class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        for participant in self.participants:
            participant.time = self.full_distance/participant.speed
            finishers.update({participant.time:participant})
        finish_list = sorted(finishers.items())
        result = {}
        place = 1
        for f in finish_list:
            result.update({place:(f[1]).name})
            place += 1
        return result