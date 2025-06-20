import main

opcao = int(input('Digite:\n 1 - Consultar filmes\n 2 - Alugar filme\n 3 - Devolver filme\n Escolha: '))

match opcao:
    case 1:
        main.consulta()
    case 2:
        id = int(input('Informe o filme que deseja alugar: '))
        main.aluga(id)
    case 3:
        id = int(input('Informe o filme que deseja devolver: '))
        main.devolve(id)