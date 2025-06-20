# importa arquivo de conexao
import conexao

# conecta cursor mysql
cursor = conexao.conexao.cursor()

# retorna lista de filmes
def consulta():
    cursor.execute('select * from filmes')

    resultado = cursor.fetchall()
    for row in resultado:
        print(row)

    conexao.conexao.close()
    cursor.close()

# aluga filme de acordo com o id e status
def aluga(id):
    try:
        cursor.execute('select status from filmes where id = %s', (id,))
        resultado = cursor.fetchone()

        # verifica status do filme para alugar
        if not resultado:
            print('Filme não encontrado!')
        elif resultado[0] != 'disponível':
            print('Filme indisponível no momento!')
        else:
            cursor.execute('update filmes set status = %s where id = %s', ('alugado', id))
            conexao.conexao.commit()
            print('Filme alugado com sucesso!')
    except Exception as e:
        print(f'Error: {e}') # em caso de erro este bloco é executado
    finally:
        conexao.conexao.close()
        cursor.close() #fecha as conexões

# devolve o filme de acordo com o id e o status
def devolve(id):
    try:
        cursor.execute('update filmes set status = %s where id = %s and status = %s', ('disponível', id, 'alugado'))
        conexao.conexao.commit()
        print(f'Filme devolvido com sucesso!')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        conexao.conexao.close()
        cursor.close()