#1 Criar uma Classe Pessoa
class Pessoa:
    def __init__ (self, nome, idade, peso, altura, sexo):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.sexo = sexo

    def descrever(self):
        return self.nome, self.idade, self.peso, self.altura, self.sexo
    
    #3 Crie um novo método
    def envelhecer(self):
        idade = self.idade + 1
        print(idade)

    #4 Comparar Idades
    def comparar_idade(self):
        if self.idade == self.idade:
            print(f"A pessoa tem a mesma idade que {self.nome}")
        elif self.idade > self.idade:
            print(f"A pessoa é mais nova que {self.nome}")
        else:
            print(f"A pessoa é mais velha que {self.nome}")
    
#2 Criar Objeto Pessoa
pessoa0 = Pessoa("Lucas", 20, 70, 1.73, "masculino")
pessoa1 = Pessoa("Eu", 20, 70, 1.73, "masculino")
pessoa2 = Pessoa("Tu", 18, 68, 1.61, "minhavida")
pessoa3 = Pessoa("Nós", 1000, 999999, 999999, "amor")
pessoa4 = Pessoa("Meu", 18, 68, 1.61, "você")
pessoa5 = Pessoa("Vós", 20, 70, 1.70, "vários")
pessoa6 = Pessoa("Eles", 20, 70, 1.73, "masculino")
pessoa7 = Pessoa("Elas", 20, 70, 1.73, "feminino")
pessoa8 = Pessoa("Todos", 999, 1000, 1000000, "todes")
pessoa9 = Pessoa("Ninguém", 0, 0, 0, "?")

pessoa0.descrever()

pessoa0.envelhecer()
pessoa0.comparar_idade()

#5 Criar uma Lista de Pessoas
lista_de_ppl = [pessoa0, pessoa1, pessoa2, pessoa3, pessoa4, pessoa5, pessoa6, pessoa7, pessoa8, pessoa9]