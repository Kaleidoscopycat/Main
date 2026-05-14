class Baleia(Animal):
    def __init__(self, cabeca, vertebra, membro_de_locomoção, espiraculo):
        super().__init__(cabeca, vertebra, membro_de_locomoção)
        self.espiraculo = espiraculo