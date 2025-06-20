# cria catálogo de filmes
filmes = {
    1: {'nome': 'Jurassic Park', 'ano': 1993, 'status': 'disponível' },
    2: {'nome': 'Harry Potter e a Pedra Filosofal', 'ano': 2001, 'status': 'alugado'},
    3: {'nome': 'Star Wars: A ameaça fantasma', 'ano': 1999, 'status': 'indisponível'}
}

# consulta catalogo de filmes
def consulta_filmes():
    for consulta, filme in filmes.items():
        print(consulta, filme)

# escolher filme para alugar
def aluga_filme(aluga):
    for chave in filmes:
        if chave == aluga and filmes[chave]['status'] == 'disponível':
           filmes[chave].update({'status': 'alugado'})
    return filmes.get(aluga, 'error')

# devolver filme alugado
def devolve_filme(devolve):
    for chave in filmes:
        if chave == devolve and filmes[chave]['status'] == 'alugado':
            filmes[chave].update({'status': 'disponível'})
    return filmes.get(devolve, 'error')