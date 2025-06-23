import conexao

cursor = conexao.conexao.cursor()

# funções de inicialização o database filmes
def create_table():
    cursor.execute('CREATE TABLE tb_filmes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome_filme TEXT NOT NULL, ano INTEGER, status TEXT NOT NULL)')
    conexao.conexao.commit()
    print('tabela criada com sucesso')

def insert_filmes():
    data = [
        ('Jurassic Park', 1993, 'disponível'),
        ('Harry Potter', 2001, 'alugado'),
        ('Star Wars: Ameaça Fantasma', 1999, 'indisponível')
    ]

    inserts = 'INSERT INTO tb_filmes(nome_filme, ano, status) VALUES(?, ?, ?)'
    cursor.executemany(inserts, data)

def consultar():
    cursor.execute('SELECT * FROM tb_filmes')

    resultado = cursor.fetchall()
    for row in resultado:
        print(row)

def alugar(id):
    try:
        cursor.execute('SELECT status FROM tb_filmes WHERE id = ?', (id,))
        resultado = cursor.fetchone()

        if not resultado:
            print('Filme não encontrado!')
        elif resultado[0] != 'disponível':
            print('Filme indisponível no momento!')
        else:
           cursor.execute('UPDATE tb_filmes SET status = ? WHERE id = ?', ('alugado', id))
           conexao.conexao.commit()
           print('Filme alugado com sucesso!')
           
    except Exception as e:
        print(f'Error: {e}')

def devolver(id):
    try:
        cursor.execute('UPDATE tb_filmes SET status = ? WHERE id = ? and status = ?', ('disponível', id, 'alugado'))
        conexao.conexao.commit()
        print(f'Filme devolvido com sucesso!')
    except Exception as e:
        print(f'Error: {e}')