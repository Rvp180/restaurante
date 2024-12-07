from reserva import Reserva

class GerenciadorReservas:
    def __init__(self):
        self.__reservas = []

    def adicionar_reserva(self, nome_cliente, data_hora, num_pessoas, mesa):
        if self.verificar_disponibilidade(data_hora, mesa):
            nova_reserva = Reserva(nome_cliente, data_hora, num_pessoas, mesa)
            self.__reservas.append(nova_reserva)
            print("Reserva realizada com sucesso!")
        else:
            print("A mesa já está reservada para este horário.")

    def listar_reservas(self):
        if not self.__reservas:
            print("Não há reservas cadastradas.")
        else:
            for i, reserva in enumerate(self.__reservas, 1):
                print(f"{i}. Cliente: {reserva.get_nome_cliente()} | Data e Hora: {reserva.get_data_hora()} "
                      f"| Pessoas: {reserva.get_num_pessoas()} | Mesa: {reserva.get_mesa()}")

    def atualizar_reserva(self, indice, nome_cliente=None, data_hora=None, num_pessoas=None, mesa=None):
        if 0 <= indice < len(self.__reservas):
            reserva = self.__reservas[indice]
            if nome_cliente:
                reserva.set_nome_cliente(nome_cliente)
            if data_hora:
                if self.verificar_disponibilidade(data_hora, mesa or reserva.get_mesa()):
                    reserva.set_data_hora(data_hora)
                else:
                    print("A nova data e horário não estão disponíveis.")
                    return
            if num_pessoas:
                reserva.set_num_pessoas(num_pessoas)
            if mesa:
                if self.verificar_disponibilidade(reserva.get_data_hora(), mesa):
                    reserva.set_mesa(mesa)
                else:
                    print("A nova mesa não está disponível.")
                    return
            print("Reserva atualizada com sucesso!")
        else:
            print("Reserva não encontrada.")

    def cancelar_reserva(self, indice):
        if 0 <= indice < len(self.__reservas):
            self.__reservas.pop(indice)
            print("Reserva cancelada com sucesso!")
        else:
            print("Reserva não encontrada.")

    def verificar_disponibilidade(self, data_hora, mesa):
        for reserva in self.__reservas:
            if reserva.get_data_hora() == data_hora and reserva.get_mesa() == mesa:
                return False
        return True
