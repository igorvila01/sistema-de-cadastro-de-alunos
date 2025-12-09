alunos={}
def adicionar_aluno(nome, idade, curso):
    alunos[nome]= {'idade': idade,
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

def listar_alunos():
    ...

