class Gato(Animal):
    def __init__(self, cabeca, vertebra, membro_de_locomoção, bigode):
        super().__init__(cabeca, vertebra, membro_de_locomoção)
        self.bigode = bigode
