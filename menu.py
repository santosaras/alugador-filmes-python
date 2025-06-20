from main import consulta_filmes,aluga_filme, devolve_filme

opcao = int(input('Digite:\n 1 - Consultar filmes\n 2 - Alugar filme\n 3 - Devolver filme\n Escolha: '))

match opcao:
    case 1:
        consulta_filmes()
    case 2:
        aluga = int(input('Informe o filme que deseja alugar: '))
        print(aluga_filme(aluga))
    case 3:
        devolve = int(input('Informe o filme que deseja devolver: '))
        print(devolve_filme(devolve))
