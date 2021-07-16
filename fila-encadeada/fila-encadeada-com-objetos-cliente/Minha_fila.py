from No_fila import No_fila

class Minha_fila: 
    def __init__(self):
        self.__inicio = None
        self.__fim = None

    def push(self, numero_cartao, nome, motivo_atendimento, senha, hora_atendimento):
        temp = No_fila(numero_cartao, nome, motivo_atendimento, senha, hora_atendimento) 
        if self.__fim:
            self.__fim.set_proximo(temp)
            self.__fim = temp
        else:
            self.__inicio = self.__fim = temp

    def visualizar_todos(self, tipo):
        if self.__inicio:
            saida = "\n\nFila: \n"
            fila_aux = self.__inicio
            if tipo == 0:
                while fila_aux:
                    saida+= fila_aux.get_nome() + " de senha: " + str(fila_aux.get_senha()) + " precisa: " + fila_aux.get_motivo_atendimento() + "\n"
                    fila_aux = fila_aux.get_proximo()
            else:
                while fila_aux:
                    saida+= fila_aux.get_nome() + " de senha: " + str(fila_aux.get_senha()) + " foi atendido as: " + str(fila_aux.get_hora_atendimento()) + " para: " + fila_aux.get_motivo_atendimento() + "\n"
                    fila_aux = fila_aux.get_proximo()
            print(saida, "\n\n")
        else: 
            print("Não há nomes para visualizar.")

    def atender(self):
        if self.__inicio:
            proximo = self.__inicio
            print("Cliente " + proximo.get_nome() + " de senha número " + str(proximo.get_senha()) + " dirija-se ao caixa XX para atendimento!")
            proximo.set_hora_atendimento()
            self.__inicio = self.__inicio.get_proximo()
            if not self.__inicio:
                self.__fim = None
            return proximo
        else:
            print("Não há próximo para atender.")