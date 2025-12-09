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
    print(entrada)


    break