# Aula 02 Arquivos
# ----------------------------------------------------------------------------------------
# abrir um arquivo para escrita
with open('arquivo.txt', 'w', text.encode("utf-8")) as file:
    file.write('Olá, Mundo!')

# abrir um arquivo para leitura e escrita
with open ('arquivo.txt', 'r+') as file:
    conteudo = file.read()
    file.write('\nAdicionando mais conteúdo.')

# brir um arquivo para anexo
    with open('arquivo.txt', 'a') as file:
        file.write('\nMais uma linha no final do arquivo.')