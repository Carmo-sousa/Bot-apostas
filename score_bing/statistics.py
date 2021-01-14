""" Responsável por filtrar os dados vindos da API https://lv.scorebing.com/ajax/score/data """


from typing import List


class Statistics:
    def __init__(self, league: dict) -> None:
        self.status: str = league.get("status", "")
        _league: dict = league.get("league", {})
        self.league_id: str = league.get("id", "")
        self.league_name: str = _league.get("fn", "")
        self._events_graph: dict = league.get("events_graph", {})
        self._events: List[dict] = self._events_graph.get("events", [])
        self._host: dict = league.get("host", {})
        self._guest: dict = league.get("guest", {})
        self._plus: dict = league.get("plus", {})

    @property
    def host(self) -> dict:
        host: dict = {
            "name": self._host.get("n"),
            "on_target": self._plus.get("hso", 0),
            "off_target": self._plus.get("hsf", 0),
            "danger_attacks": self._plus.get("hd", 0),
            "attacks": self._plus.get("ha", 0),
            "possession": self._plus.get("hqq", 0),
            "corners": self.events("hc"),
            "goals": self.events("hg"),
        }
        return host

    @property
    def guest(self) -> dict:
        guest: dict = {
            "name": self._guest.get("n"),
            "on_target": self._plus.get("gso", 0),
            "off_target": self._plus.get("gsf", 0),
            "danger_attacks": self._plus.get("gd", 0),
            "attacks": self._plus.get("ga", 0),
            "possession": self._plus.get("gqq", 0),
            "corners": self.events("gc"),
            "goals": self.events("gg"),
        }
        return guest

    def events(self, event_type: str) -> int:
        total_events: int = 0

        for event in self._events:
            type: str = event.get("t", "")

            if type == event_type:
                total_events += 1

        return total_events
