# cria catálogo de filmes
filmes = {
    1: {'nome': 'Jurassic Park', 'ano': 1993, 'status': 'disponível' },
    2: {'nome': 'Harry Potter e a Pedra Filosofal', 'ano': 2001, 'status': 'disponível'},
    3: {'nome': 'Star Wars: A ameaça fantasma', 'ano': 1999, 'status': 'indisponível'}
}

# consultar catálogo de filmes
for chave, valor in filmes.items():
        print(chave, valor)

# escolher filme para assistir
aluga = int(input('Informe o filme que deseja alugar: '))

for chave in filmes:
    if chave == aluga and filmes[chave]['status'] == 'disponível':
        filmes[chave].update({'status': 'alugado'})

print(filmes) # verificando se o status foi atualizado

# devolver filme alugado
devolve = int(input('Informe o filme que deseja devolver: '))

for chave in filmes:
    if chave == devolve and filmes[chave]['status'] == 'alugado':
        filmes[chave].update({'status': 'disponível'})

print(filmes) # verificando se o status foi atualizado

# remove o filme indisponível do catálogo
aluga = int(input('Informe o filme que deseja alugar: '))

chave_remove = []

for chave in filmes:
    if chave == aluga and filmes[chave]['status'] == 'indisponível':
        chave_remove.append(chave)

for chave in chave_remove:
    filmes.pop(chave)

print(filmes) # verifica se o filme foi removido