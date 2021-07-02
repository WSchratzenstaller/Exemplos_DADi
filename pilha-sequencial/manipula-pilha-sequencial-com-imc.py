class Minha_pilha: 
    def __init__(self):
        self.__pilha = []
 
    def push(self, imc):
        self.__pilha.append(imc)
 
    def pop(self):
        if self.__pilha:
            del self.__pilha[-1]
        else:
            print("Não pode remover, pilha vazia.")
 
    def print_top(self):
        if self.__pilha:
            imc_topo = self.__pilha[-1]
            print("\nElemento do topo: " + str(imc_topo))
            #Extra, exibição de análise.
            if  imc_topo < 18.5:
                print("Abaixo do esperado.")
            elif imc_topo > 24.9:
                print("Acima do esperado.")
            else:
                print("Dentro do esperado.")
        else:
            print("Pilha vazia, não há topo para imprimir.")
 
    def print_all(self): 
        if self.__pilha:
            saida= "Pilha: \n"
            pilha_temporaria=[]
            while self.__pilha:
                saida+= str(self.__pilha[-1])+ "\n"
                pilha_temporaria.append(self.__pilha[-1])
                del self.__pilha[-1]
            print(saida)
            while pilha_temporaria:
                self.__pilha.append(pilha_temporaria[-1])
                del (pilha_temporaria[-1])
        else:
            print("Não há IMCs para imprimir.")  
######
class Prova1:
    def main():
        pilha = Minha_pilha()
        while True:
            opcao = int(input("Opções:\n"
                              "1 – Incluir novo IMC na pilha.\n"
                              "2 – Excluir o último IMC da pilha.\n"
                              "3 – Imprimir o último IMC da pilha.\n"
                              "4 - Imprimir todos.\n" #(extra - não pedia na questão)
                              "5 - Sair.\n"
                              "Escolha: \n"))
            if opcao == 1:
                altura = float(input("Informe altura: "))
                peso = float(input("Informe peso: "))
                imc = peso/(altura * altura)
                pilha.push(imc)
            elif opcao == 2:
                pilha.pop()
            elif opcao == 3:
                pilha.print_top()
            elif opcao == 4:
                pilha.print_all()
            elif opcao == 5:
                break
            else:
                print("Opção inválida.")

if __name__ == '__main__':
    Prova1.main()