import os

alunos={}
ra_cont = 0

def limpa_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def adicionar_aluno(ra, nome, idade, curso):
    alunos[ra]= {'nome' : nome,
                   'idade': idade,
                   'curso': curso,
                   'notas': [],
                   'media': 0.0
                   }
    
    print('Aluno Cadastrado com Sucesso!')
    
    
def adicionar_nota(ra, nota):
    if ra in alunos:
        alunos[ra]['notas'].append(nota)

    print(f'Nota do aluno {alunos[ra]['nome']} cadastrada com sucesso!')

def remover_aluno(ra):
    if ra in alunos:
        print(f'Aluno {alunos[ra]['nome']} deletado com sucesso!')
        del alunos[ra]        
    else:
        print('Ra Inexistente!')
    

def calcular_media(ra):
    if ra in alunos and len(alunos[ra]['notas']) > 0:
        alunos[ra]['media'] = f'{sum(alunos[ra]['notas'])/len(alunos[ra]['notas']):.2f}'
    else:
        alunos[ra]['media'] = 0.0

def listar_alunos(alunos):
    print('\n---------- Lista de Alunos -------------')
    for ra, pessoa in alunos.items():
        print(f'{ra} | {pessoa['nome']} | {pessoa['idade']} anos | {pessoa['curso']} | {pessoa['notas']} | {pessoa['media']}')
    print('----------------------------------------')


menu = """
[c] Cadastrar Aluno
[n] Adicionar Nota Aluno
[d] Remover Aluno
[m] Calcular Media Aluno 
[l] Listar Alunos
[s] Sair
=>"""

while True:
    entrada = input(menu)[0].lower()
    
    match entrada:
        case 'c':
            while True:
                try:
                    nome = input('Nome Aluno: ').upper()
                    idade = int(input('Idade Aluno: '))
                    curso = input('Curso: ').upper()
                    ra_cont += 1

                    limpa_tela()
                    adicionar_aluno(ra_cont, nome, idade, curso)                    
                    break
                
                except ValueError:
                    print('Idade Inválida, preencha novamente!')
                    continue                        

        case 'n':
            limpa_tela()
            listar_alunos(alunos)

            print('Cadastrar Nota!')
            while True:
                try:
                    ra_entrada = int(input('Digite o RA do Aluno: '))

                    if ra_entrada in alunos:
                        nota = float(input('Digite a Nota:'))
                    else:
                        print('Aluno nao existe!')
                        break
                    
                    limpa_tela()
                    adicionar_nota(ra_entrada, nota)
                    break

                except ValueError:
                    print('Entrada Invalida!') 
                    opcao = input('Digite 1 para tentar novamente\n' \
                                  'Ou qualquer coisa para menu anterior')  

                    if opcao == 1:
                        continue
                    else:
                        break                               
        
        case 'd':
            limpa_tela()
            listar_alunos(alunos)

            print()
            while True:
                try:
                    ra_entrada = int(input('Digite o RA do Aluno: '))

                    limpa_tela()
                    remover_aluno(ra_entrada)
                    break

                except ValueError:
                    print('Entrada Invalida!') 
                    opcao = input('Digite 1 para tentar novamente\n' \
                                  'Ou qualquer coisa para menu anterior')  

                    if opcao == 1:
                        continue
                    else:
                        break 
        
        case 'm':
            limpa_tela()
            listar_alunos(alunos)

            print()
            while True:
                try:
                    ra_entrada = int(input('Digite o RA do Aluno: '))

                    limpa_tela()
                    calcular_media(ra_entrada)
                    break

                except ValueError:
                    print('Entrada Invalida!') 
                    opcao = input('Digite 1 para tentar novamente\n' \
                                  'Ou qualquer coisa para menu anterior')  

                    if opcao == 1:
                        continue
                    else:
                        break 
        
        case 'l':
            listar_alunos(alunos)
        
        case 's':
            break

        case _:
            print('Entrada Inválida! Tente Novamente!')
            continue

    

    