class Team:
    def __init__(self, nome):
        self.nome = nome

    @property
    def nome(self):
        return self.nome

    @property.nome
    def nome(self, nome):
        self.nome = nome
