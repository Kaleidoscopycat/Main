#1.1 Criar uma Classe Pessoa
class Pessoa:
    def __init__ (self, nome, idade, peso, altura, sexo):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.sexo = sexo

    def descrever(self):
        return self.nome, self.idade, self.peso, self.altura, self.sexo
    
    #1.3 Crie um novo método
    def envelhecer(self):
        return self.idade + 1

    #1.4 Comparar Idades
    def comparar_idade(self):
        if self.idade == self.idade:
            print(f"A pessoa tem a mesma idade que {self.nome}")
        elif self.idade > self.idade:
            print(f"A pessoa é mais nova que {self.nome}")
        else:
            print(f"A pessoa é mais velha que {self.nome}")
    
#1.2 Criar Objeto Pessoa
pessoa0 = Pessoa("Luck", 20, 70, 1.73, "masculino")
pessoa1 = Pessoa("Gray", 20, 70, 1.73, "Feminino")
pessoa2 = Pessoa("Erick", 18, 68, 1.61, "Masculino")
pessoa3 = Pessoa("Stuart", 6, 10, 1.40, "Masculino")
pessoa4 = Pessoa("Bob", 4, 68, 0.90, "Masculino")
pessoa5 = Pessoa("Kevin", 20, 70, 1.70, "Masculino")
pessoa6 = Pessoa("Alex", 20, 70, 1.73, "Feminino")
pessoa7 = Pessoa("Steve", 20, 70, 1.73, "Masculino")
pessoa8 = Pessoa("Walter", 30, 70, 1.90, "Masculino")
pessoa9 = Pessoa("White", 3, 1, 0.10, "Masculino")

print(pessoa0.descrever())

pessoa0.envelhecer()
pessoa0.comparar_idade()

#1.5 Criar uma Lista de Pessoas
lista_de_ppl = [pessoa0, pessoa1, pessoa2, pessoa3, pessoa4, pessoa5, pessoa6, pessoa7, pessoa8, pessoa9]

#2.1 Criar uma Classe Veículo
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def info(self):
        return self.marca, self.modelo, self.ano

    #2.3 atualizar ano
    def atualizar_ano():
        self.ano = int(input("Insira o ano atualizado do veículo:"))

    #2.4
    def comparar(self, v2):
        if self.ano > v2.ano:
            print(f"{self} é mais novo")
        elif self.ano < v2.ano:
            print(f"{v2} é mais novo")
        else:
            print("ambos são do mesmo ano")

#2.2 criar um Objeto Veiculo
TRL5O57 = Veiculo("Ford", "Focus", 2020)
TRS5O57 = Veiculo("Ford", "Focus", 2005)
TRV5O57 = Veiculo("Ford", "Focus", 2015)
TRT5O57 = Veiculo("Ford", "Focus", 2010)


#2.5 criar uma lista de Veiculos
lista_de_veiculos = [TRL5O57, TRS5O57, TRV5O57, TRT5O57]

TRL5O57.info()
TRL5O57.atualizar_ano()
TRL5O57.comparar()


#desafio
class Falar:
    def __init__(self, assunto, conteudo, entonacao, volume):
        self.assunto = assunto
        self.conteudo = conteudo
        self.entonacao = entonacao
        self.volume = volume

        def conversar(self, pessoas):
            return f"{self} conversa {self.volume} com {pessoas} sobre {self.assunto} de forma {self.entonacao}"
        def discursar(self, interlocutores):
           return f"{self} disse para os {interlocutores}, {self.volume} e {self.entoncao}: {self.conteudo}\nos {interlocutores} ficaram {self.entonacao}"
        def cantar(self):
            return f"{self} canta {self.assunto} {self.volume} bastante {entonacao}"
        
vitor = Falar("gases", "abobrinha", "revoltado", "muito alto")
nina = Falar("Happier Than Ever", "alto", "alegre")
leo =  Falar ("Python", "Vitor, larga de ser um usuário! jesus.", "esbravejado", "alto")
alunos = Falar("","","espantados","")

grupo = ["nina","leo"]
vitor.conversar(grupo)
leo.discursar(alunos)
nina.cantar()
