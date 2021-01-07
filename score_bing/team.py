""" Separa os dados do time e faz os cálculos """


class Team:
    def __init__(self, team, time):
        self._time = int(time)
        self.name = team["name"]
        self.on_target = team["on_target"]
        self.off_target = team["off_target"]
        self.attacks = team["attacks"]
        self.danger_attack = team["danger_attacks"]
        self.possession = team["possession"]
        self.corners = team["corners"]
        self.goals = team["goals"]

    @property
    def apm(self):
        return int(self.danger_attack) / self._time

    @property
    def opportunity_goals(self):
        return int(self.corners) + int(self.on_target) + int(self.off_target)

    def is_possession(self):
        if self.possession >= 60:
            return True

        else:
            return False
