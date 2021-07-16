from Minha_fila import Minha_fila
from Dados_atendimento import Dados_atendimento

class Fila_sequencial:
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
    Fila_sequencial.main()