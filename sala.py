alunos={}
ra = 0
def adicionar_aluno(ra, nome, idade, curso):
    alunos[ra]= {'nome' : nome,
                   'idade': idade,
                   'curso': curso,
                   'notas': []
                   }
    
    
def adicionar_nota(ra, nota):
    if ra in alunos:
        alunos[ra]['notas'].append(nota)

def remover_aluno(ra):
    if ra in alunos:
        del alunos[ra]
        print('Aluno deletado com sucesso!')
    else:
        print('Ra Inexistente!')
    

def calcular_media(ra):
    ...

def listar_alunos(alunos):
    for ra, pessoa in alunos.items():
        print(ra, pessoa['nome'], pessoa['idade'], pessoa['curso'], pessoa['notas'])


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

                    ra += 1
                    adicionar_aluno(ra, nome, idade, curso)
                    break
                
                except ValueError:
                    print('Idade Inválida, preencha novamente!')
                    continue                        

        case 'n':
            listar_alunos(alunos)

            print('Cadastrar Nota!')
            while True:
                try:
                    ra = int(input('Digite o RA do Aluno: '))

                    if ra in alunos:
                        nota = float(input('Digite a Nota:'))
                    else:
                        print('Aluno nao existe!')
                        break

                    adicionar_nota(ra, nota)
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
            listar_alunos(alunos)

            print()
            while True:
                try:
                    ra = int(input('Digite o RA do Aluno: '))

                    remover_aluno(ra)
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
            listar_alunos(alunos)

            print()
            while True:
                try:
                    ra = int(input('Digite o RA do Aluno: '))

                    calcular_media(ra)
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

    

    