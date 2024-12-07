from gerenciador_reservas import GerenciadorReservas

gerenciador = GerenciadorReservas()

while True:
    print("\nSistema de Reservas")
    print("1. Adicionar Reserva")
    print("2. Listar Reservas")
    print("3. Atualizar Reserva")
    print("4. Cancelar Reserva")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do cliente: ")
        data_hora = input("Digite a data e hora (dd/mm/aaaa hh:mm): ")
        num_pessoas = int(input("Digite o número de pessoas: "))
        mesa = int(input("Digite o número da mesa: "))
        gerenciador.adicionar_reserva(nome, data_hora, num_pessoas, mesa)

    elif opcao == "2":
        gerenciador.listar_reservas()

    elif opcao == "3":
        gerenciador.listar_reservas()
        indice = int(input("Digite o número da reserva que deseja atualizar: ")) - 1
        print("Deixe em branco para manter os dados atuais.")
        nome = input("Novo nome do cliente: ")
        data_hora = input("Nova data e hora (dd/mm/aaaa hh:mm): ")
        num_pessoas = input("Novo número de pessoas: ")
        mesa = input("Nova mesa: ")
        gerenciador.atualizar_reserva(
            indice,
            nome or None,
            data_hora or None,
            int(num_pessoas) if num_pessoas else None,
            int(mesa) if mesa else None
        )

    elif opcao == "4":
        gerenciador.listar_reservas()
        indice = int(input("Digite o número da reserva que deseja cancelar: ")) - 1
        gerenciador.cancelar_reserva(indice)

    elif opcao == "5":
        print("Saindo do sistema. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
