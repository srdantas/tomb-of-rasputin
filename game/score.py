import time


class Score:

    def __init__(self, name):
        self.name = name
        self.level_score = 0
        self.kills = 0
        self.start_time = 0
        self.end_time = 0

    def start_adventure(self, level_score):
        self.level_score = level_score
        self.start_time = time.time()

    def add_level_score(self, level_score):
        self.level_score = level_score

    def add_kill(self):
        self.kills += 1

    def calculate_score(self):
        self.end_time = time.time()
        total_time = self.end_time - self.start_time
        return "{0:.2f}".format((self.kills * self.level_score) / total_time)
