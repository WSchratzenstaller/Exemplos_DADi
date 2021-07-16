from Minha_fila import Minha_fila

class Fila_encadeada_principal:
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
                fila_aguardando.push(numero_cartao, nome, motivo_atendimento, senha, None)
            elif opcao == 2:
                atendido = fila_aguardando.atender()
                if atendido:
                    fila_atendidos.push(atendido.get_numero_cartao(), atendido.get_nome(), atendido.get_motivo_atendimento(), atendido.get_senha(), atendido.get_hora_atendimento())
            elif opcao == 3:
                fila_aguardando.visualizar_todos(0)
            elif opcao == 4:
                fila_atendidos.visualizar_todos(1)
            elif opcao == 5:
                break
            else:
                print("Opção inválida.")

if __name__ == '__main__':
    Fila_encadeada_principal.main()