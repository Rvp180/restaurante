class Reserva:
    def __init__(self, nome_cliente, data_hora, num_pessoas, mesa):
        self.__nome_cliente = nome_cliente
        self.__data_hora = data_hora
        self.__num_pessoas = num_pessoas
        self.__mesa = mesa

    # Getters
    def get_nome_cliente(self):
        return self.__nome_cliente

    def get_data_hora(self):
        return self.__data_hora

    def get_num_pessoas(self):
        return self.__num_pessoas

    def get_mesa(self):
        return self.__mesa

    # Setters
    def set_nome_cliente(self, nome_cliente):
        self.__nome_cliente = nome_cliente

    def set_data_hora(self, data_hora):
        self.__data_hora = data_hora

    def set_num_pessoas(self, num_pessoas):
        self.__num_pessoas = num_pessoas

    def set_mesa(self, mesa):
        self.__mesa = mesa
