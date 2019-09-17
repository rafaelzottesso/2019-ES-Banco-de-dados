# Importa a biblioteca do sqlite para usar o banco
import sqlite3

# Procedimento que recebe uma conexão e cria uma tabela
def criar_tabela_usuario(conexao):

    # Cursor é a estrutura de controle que percorre os registros do banco
    # Fazemos uma chamada ele para podermos executar nosso SQL
    cursor = conexao.cursor()

    # Monta o SQL a ser executado
    sql = '''CREATE TABLE IF NOT EXISTS usuario (
                nome TEXT NOT NULL,
                login TEXT NOT NULL,
                senha TEXT NOT NULL
            ); '''
    
    # Executa o SQL
    cursor.execute(sql)

# Procedimento que recebe a conexão
def inserir_usuario(conexao):

    # Pede os dados para o usuário
    nome = input("Nome: ")
    login = input("Login: ")
    senha = input("Senha: ")

    # Cria o cursor
    cursor = conexao.cursor()

    # Monta o SQL
    sql = '''
        INSERT INTO usuario VALUES(
            '{}',
            '{}',
            '{}'
        );
    '''.format(nome, login, senha)

    # Executa
    cursor.execute(sql)

    # Quanto insere, altera ou exclui tem que fazer o commit
    # Que é como se fosse um "salvar" para registrar as alterações feitas
    conexao.commit()


def listar_usuarios(conexao):
    # Cria o cursor
    cursor = conexao.cursor()
    # Monta o SQL
    # Toda tabela tem o rowid que é o ID de cada registro, mesmo sem você criar
    sql = """
        SELECT rowid, * FROM usuario;
    """
    # Executar o SQL
    cursor.execute(sql)

    # Depois de executar o SQL, precisa converter os registros encontrados em alguma forma
    # que o Python possa percorrer esses dados. Assim, o fetchall() transforma os dados
    # em um vetor com todos os registros. 
    # Cada registro por sua vez também é um vetor e cada coluna é uma posição, ou a ordem do SELECT que você fez.
    lista = cursor.fetchall()

    # Mostra a linha de título da tabela
    print("ID\t Nome\t\t\t Login")

    # "lista" é um vetor com todos os registros
    # "u" vai ser cada linha encontrada no select
    # Este for faz +- isso: u = lista[0], u = lista[1], u = lista[2], ...
    for u in lista:
        # O "u" é um vetor e cada coluna/ordem do select é uma coluna
        # SELET rowid, *
        # Neste caso, u[0] é o rowid, u[1] é o nome, u[2] é o login e u[3] é a senha
        print("{}\t {}\t {}".format(u[0], u[1], u[2]))        
        

################################
###### Programa principal ######
################################

# Cria a conexão com o banco de dados
conexao = sqlite3.connect("banco.sqlite")

# Executa o procedimento
# criar_tabela_usuario(conexao)

# Executa o procedimento
# inserir_usuario(conexao)

# Listar usuários
listar_usuarios(conexao)

# Fecha a conexão
conexao.close()
