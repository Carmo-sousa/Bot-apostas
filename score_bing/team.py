"""
Separa os dados do time e faz os cálculos
"""


class Team:
    def __init__(self, team: dict, time: str) -> None:
        self._time: int = int(time)
        self.name: str = team["name"]
        self.on_target: str = team["on_target"]
        self.off_target: str = team["off_target"]
        self.attacks: str = team["attacks"]
        self.danger_attack: str = team["danger_attacks"]
        self.possession: int = int(team["possession"])
        self.corners: str = team["corners"]
        self.goals: str = team["goals"]

    @property
    def apm(self) -> float:
        """ Return attacks per minute """
        return int(self.danger_attack) / self._time

    @property
    def opportunity_goals(self) -> int:
        return int(self.corners) + int(self.on_target) + int(self.off_target)

    def is_possession(self) -> bool:
        if self.possession >= 60:
            return True

        else:
            return False
