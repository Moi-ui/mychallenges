import psycopg2

# Dados da conexão com o PostgreSQL
import psycopg2

conexao = psycopg2.connect(
    dbname="biblioteca",
    user="postgres",
    password="sua_senha",
    host="localhost",
    port="5432"
)


cursor = conexao.cursor()

# Inserir livro
def adicionar_livro(titulo, autor, ano):
    cursor.execute(
        "INSERT INTO livros (titulo, autor, ano) VALUES (%s, %s, %s)",
        (titulo, autor, ano)
    )
    conexao.commit()
    print("Livro adicionado com sucesso.")

# Listar todos os livros
def listar_livros():
    cursor.execute("SELECT * FROM livros")
    for livro in cursor.fetchall():
        print(livro)

# Exemplo de uso
adicionar_livro("1984", "George Orwell", 1949)
listar_livros()

# Fechar conexões
cursor.close()
conexao.close()