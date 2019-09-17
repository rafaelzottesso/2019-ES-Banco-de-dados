# Importa a biblioteca do sqlite para usar o banco
import sqlite3

# Importa tudo que tem no arquivo "usuario.py"
import usuario

################################
###### Programa principal ######
################################

# Cria a conexão com o banco de dados
conexao = sqlite3.connect("banco.sqlite")

# Executa o procedimento
# criar_tabela_usuario(conexao)

# Executa o procedimento
# usuario.inserir_usuario(conexao)


# Listar usuários
usuario.listar_usuarios(conexao)


# Fecha a conexão
conexao.close()
