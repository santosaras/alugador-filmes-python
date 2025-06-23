import main

# main.create_table()
# main.insert_filmes()

while True:
    opcao = int(input('Digite:\n1 - Consultar Filmes\n2 - Alugar Filme\n3 - Devolver Filme\n4 - Sair:  '))
    match opcao:
        case 1:
            main.consultar()
        case 2:
            id = int(input('Informe o filme que deseja alugar: '))
            main.alugar(id)
        case 3:
            id = int(input('Informe o filme que deseja devolver: '))
            main.devolver(id)
        case 4:
            print('Encerrando programa')
            break
        case _:
            print('Opção inválida! Por favor digite uma opoção de 1 a 4!')