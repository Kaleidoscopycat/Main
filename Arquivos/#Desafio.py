#Desafio
nome = 'lucas'
with open('meuarquivo.txt', 'w') as file:
    file.write(f'Olá Mundo!\nEste é um arquivo de texto.\nCriado por {nome}')

with open ('meuarquivo.txt', 'r') as file:
    conteudo = file.read()
    print(conteudo)

def contadordepalavras(n):
    with open (n, 'r') as file:
        conteudo = file.read()
        palavras = conteudo.split()
        print('\nO arquivo possui', len(palavras), 'palavras')
contadordepalavras('meuarquivo.txt')

def concatenadordearquivos(n,m):
    file1 = 'a'
    file2 = 'b'
    
    with open(n,'r') as a:
        file1 = a.read()
    with open(m,'r') as b:
        file2 = b.read()
    with open ('ArquivoAB', 'w') as c:
        file3 = a + b
        c.write(file3)
        print(file3)
concatenadordearquivos('arquivo.txt', 'meuarquivo.txt')
    