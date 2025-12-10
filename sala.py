alunos={}
def adicionar_aluno(nome, idade, curso):
    ra = len(alunos)+1
    alunos[ra]= {'nome' : nome,
                   'idade': idade,
                   'curso': curso,
                   'notas': []
                   }
    
    
def adicionar_nota(nome, nota):
    if nome in alunos:
        alunos[nome]['notas'].append(nota)

def remover_aluno():
    ...

def calcular_media():
    ...

def listar_alunos(alunos):
    for ra, pessoa in alunos.items():
        print(ra, pessoa['nome'], pessoa['idade'], pessoa['curso'])


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

                    adicionar_aluno(nome, idade, curso)
                    break
                
                except ValueError:
                    print('Idade Inválida, preencha novamente!')
                    continue                        

        case 'n':
            ...
        
        case 'd':
            ...
        
        case 'm':
            ...
        
        case 'l':
            listar_alunos(alunos)
        
        case 's':
            break

        case _:
            print('Entrada Inválida! Tente Novamente!')
            continue

    

    