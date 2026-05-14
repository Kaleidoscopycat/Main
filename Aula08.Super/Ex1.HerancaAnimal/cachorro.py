class Cachorro(Animal):
    def __init__(self, cabeca, vertebra, membro_de_locomoção, focinho):
        super().__init__(cabeca, vertebra, membro_de_locomoção)
        self.focinho = focinho