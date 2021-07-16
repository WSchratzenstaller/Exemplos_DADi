class Minha_fila: 
    def __init__(self):
        self.__fila = []
 
    def push(self, cliente):
        self.__fila.append(cliente)
 
    def atender(self):
        if self.__fila:
            proximo = self.__fila[0]
            print("Cliente " + proximo.get_nome() + " de senha número " + str(proximo.get_senha()) + " dirija-se ao caixa XX para atendimento!")
            proximo.set_hora_atendimento()
            del self.__fila[0]
            return proximo
        else:
            print("Não há ninguém para atender.")
 
    def visualizar_todos(self, tipo): 
        if self.__fila:
            saida= "Fila: \n"
            fila_temporaria=[]
            if tipo == 0:
                while self.__fila:
                    proximo = self.__fila[0]
                    saida+= proximo.get_nome() + " de senha: " + str(proximo.get_senha()) + " precisa: " + proximo.get_motivo_atendimento() + "\n"
                    fila_temporaria.append(proximo)
                    del self.__fila[0]
            else:
                while self.__fila:
                    proximo = self.__fila[0]
                    saida+= proximo.get_nome() + " de senha: " + str(proximo.get_senha()) + " foi atendido em: " + proximo.get_hora_atendimento() + " para: " + proximo.get_motivo_atendimento() + "\n"
                    fila_temporaria.append(proximo)
                    del self.__fila[0]
            print(saida)
            while fila_temporaria:
                self.__fila.append(fila_temporaria[0])
                del (fila_temporaria[0])
        else:
            print("Não há nomes para visualizar.")
