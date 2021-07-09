import time

class Dados_atendimento:
    def __init__(self, numero_cartao, nome, motivo_atendimento, senha):
        self.__numero_cartao = numero_cartao
        self.__nome = nome
        self.__motivo_atendimento = motivo_atendimento
        self.__senha = senha
        self.__hora_atendimento = None

    def set_hora_atendimento(self):
        self.__hora_atendimento = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime())

    def get_numero_cartao(self):
        return self.__numero_cartao
    
    def get_nome(self):
        return self.__nome
    
    def get_motivo_atendimento(self):
        return self.__motivo_atendimento

    def get_senha(self):
        return self.__senha 

    def get_hora_atendimento(self):
        return self.__hora_atendimento