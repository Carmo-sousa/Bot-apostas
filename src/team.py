class Team:
    def __init__(self, team: dict):
        self.name = team["name"]
        self.on_target = team["on_target"]
        self.off_target = team["off_target"]
        self.attacks = team['attacks']
        self.danger_attack = team["danger_attacks"]
        self.possessions = team["possession"]
        self.corners = team["corners"]
        self.goals = team["goals"]

    def apm(self, time):
        return int(self.danger_attack) / int(time)

    def opportunity_goals(self):
        return int(self.corners) + int(self.on_target) + int(self.off_target)
