class Statistics:
    def __init__(self, league):
        self.status = league.get("status")
        _league = league.get("league")
        self.league_id = league.get("id")
        self.league_name = _league.get("fn")
        self._events_graph = league.get("events_graph")
        self._events = self._events_graph.get("events", [])
        self._host = league.get("host")
        self._guest = league.get("guest")
        self._plus = league.get("plus")

    @property
    def host(self):
        host = {
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
    def guest(self):
        guest = {
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

    def events(self, event_type):
        total_events = 0

        for event in self._events:
            type = event.get("t")

            if type == event_type:
                total_events += 1

        return total_events
