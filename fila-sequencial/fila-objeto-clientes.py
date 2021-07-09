class Minha_fila: 
    def __init__(self):
        self.__fila = []
 
    def push(self, cliente):
        self.__fila.append(cliente)
 
    def atender(self):
        if self.__fila:
            proximo = self.__fila[0]
            print("Cliente ", proximo.get_nome(), " de senha número ", proximo.get_senha(), " dirija-se ao caixa XX para atendimento!")
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
######
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

######

class Exercicio_fila_sequencial:
    def main():
        senha = 0
        fila_aguardando = Minha_fila()
        fila_atendidos = Minha_fila()
        while True:
            opcao = int(input("Opções:\n"
                              "1 - Receber cliente na fila.\n"
                              "2 - Chamar para atendimento.\n"
                              "3 - Visualizar fila de clientes aguardando.\n"
                              "4 - Visualizar fila de clientes atendidos.\n"
                              "5 - Sair.\n"
                              "Escolha: \n"))
            if opcao == 1:
                numero_cartao = int(input("Informe número do cartão: \n"))
                nome = input("Com o número do cartão, poderiamos buscar o nome na base de dados\n"
                             "mas como não há base, informe o nome:\n")
                motivo_atendimento = input("Informe motivo do atendimento:\n") 
                senha += 1 
                cliente = Dados_atendimento(numero_cartao, nome, motivo_atendimento, senha)
                fila_aguardando.push(cliente)
            elif opcao == 2:
                atendido = fila_aguardando.atender()
                fila_atendidos.push(atendido)
            elif opcao == 3:
                fila_aguardando.visualizar_todos(0)
            elif opcao == 4:
                fila_atendidos.visualizar_todos(1)
            elif opcao == 5:
                break
            else:
                print("Opção inválida.")

if __name__ == '__main__':
    Exercicio_fila_sequencial.main()