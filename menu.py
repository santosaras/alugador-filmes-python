from main import consulta_filmes,aluga_filme, devolve_filme

opcao = int(input('Digite uma opção 1 para consultar filmes ou 2 para alugar filme:  '))

match opcao:
    case 1:
        aluga_filmes.consulta_filmes()
    case 2:
        aluga = int(input('Informe o filme que deseja alugar: '))
        aluga_filmes.aluga_filme(aluga)
    case 3:
        devolve = int(input('Informe o filme que deseja devolver: '))
        aluga_filmes.devolve_filme(devolve)
