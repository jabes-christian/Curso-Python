from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver novas pessoas', 'Cadastra nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listra um conteúdo do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema
        cabeçalho('Saindo do Sistema... Até logo!')
        break
    else:
        print('\033[31mERROR! Digite uma Opção Válida\033[m')
    sleep(2)
