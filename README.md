📚 Sistema de Gerenciamento de Alunos (CLI)
Este projeto é um sistema simples de gerenciamento de alunos desenvolvido em Python, utilizando apenas recursos básicos da linguagem e interação via linha de comando (CLI).
Ele permite cadastrar alunos, adicionar notas, calcular médias, listar e remover registros de forma prática.

🚀 Funcionalidades
- Cadastrar Aluno
- Nome, idade e curso são armazenados.
- Cada aluno recebe um RA (Registro Acadêmico) único.
- Adicionar Nota
- Permite adicionar notas entre 0 e 10 para cada aluno.
- As notas ficam registradas em uma lista associada ao aluno.
- Remover Aluno
- Exclui um aluno do sistema pelo RA.
- Calcular Média
- Calcula a média das notas cadastradas para o aluno.
- Média exibida com duas casas decimais.
- Listar Alunos
- Exibe todos os alunos cadastrados com seus dados, notas e média.
- Menu Interativo
- Interface simples via terminal com opções:
[c] Cadastrar Aluno
[n] Adicionar Nota Aluno
[d] Remover Aluno
[m] Calcular Media Aluno
[l] Listar Alunos
[s] Sair



🛠️ Tecnologias Utilizadas
- Python 3.x
- Biblioteca padrão (os) para limpar a tela.

📂 Estrutura do Código
- limpa_tela() → limpa o terminal (compatível com Windows/Linux).
- adicionar_aluno() → cadastra novo aluno.
- adicionar_nota() → adiciona nota ao aluno.
- remover_aluno() → exclui aluno pelo RA.
- calcular_media() → calcula média das notas.
- listar_alunos() → mostra todos os alunos cadastrados.
- Loop principal com menu interativo.

▶️ Como Executar
- Clone este repositório ou copie o código para um arquivo, por exemplo:
git clone https://github.com/igorvila01/sistema-de-cadastro-de-alunos.git
cd sistema-de-cadastro-de-alunos
- Execute o programa com Python:
python sala.py
- Use o menu para interagir com o sistema.

📌 Exemplo de Uso
[c] Cadastrar Aluno
[n] Adicionar Nota Aluno
[d] Remover Aluno
[m] Calcular Media Aluno
[l] Listar Alunos
[s] Sair
=>


- Cadastro de aluno:
Nome Aluno: Joao
Idade Aluno: 22
Curso: ENGENHARIA
Aluno Cadastrado com Sucesso!
- Adição de nota:
Digite o RA do Aluno: 1
Digite a Nota: 8.5
Nota do aluno IGOR cadastrada com sucesso!
- Listagem:
---------- Lista de Alunos -------------
1 | JOAO | 22 anos | ENGENHARIA | [8.5] | 8.50
----------------------------------------



💡 Melhorias Futuras
- Persistência dos dados em arquivo (JSON/CSV).
- Interface gráfica (GUI) ou web.
- Relatórios de desempenho por curso.

👨‍💻 Autor
Projeto desenvolvido por Igor como prática de programação em Python.
