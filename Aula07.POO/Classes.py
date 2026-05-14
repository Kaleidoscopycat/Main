class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def saudar(self):
        print(f" Olá meu nome é {self.nome} e tenho {self.idade} anos.")

#criando um objeto pessoa
pessoa1 = Pessoa("João", 30)
pessoa1.saudar()