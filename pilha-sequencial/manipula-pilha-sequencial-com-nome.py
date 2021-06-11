class Minha_pilha: 
    def __init__(self):
        self.__pilha = []
 
    def push(self, nome):
        self.__pilha.append(nome)
 
    def pop(self):
        if self.__pilha:
            del self.__pilha[len(self.__pilha)-1]
        else:
            print("Pilha vazia.")
 
    def print_top(self):
        if self.__pilha:
            print("\nElemento do topo: " + self.__pilha[len(self.__pilha)-1])
        else:
            print("Pilha vazia, não há topo para imprimir.")
 
    def print_all(self): 
        if self.__pilha:
            saida= "Pilha: \n"
            pilha_temporaria=[]
            while self.__pilha:
                saida+= self.__pilha[len(self.__pilha)-1]+ "\n"
                pilha_temporaria.append(self.__pilha[len(self.__pilha)-1])
                del self.__pilha[len(self.__pilha)-1]
            print(saida)
            while pilha_temporaria:
                self.__pilha.append(pilha_temporaria[len(pilha_temporaria)-1])
                del (pilha_temporaria[len(pilha_temporaria)-1])
        else:
            print("Não há nomes para imprimir.")
 
    def pop_all(self): 
        if self.__pilha:
            while self.__pilha:	
                del self.__pilha[len(self.__pilha)-1]
            print("Todos os nomes foram excluidos.")
        else: 
            print("Não há nomes para excluir.")
######
class Exercicio2:
    def main():
        pilha = Minha_pilha()
        while True:
            opcao = int(input("Opções:\n"
                              "1 – Incluir novo nome na pilha.\n"
                              "2 – Excluir o nome do topo da pilha.\n"
                              "3 – Imprimir todos os nomes da pilha.\n"
                              "4 – Imprimir o nome do topo da pilha.\n"
                              "5 – Excluir todos os nomes da pilha.\n"
                              "6 - Sair.\n"
                              "Escolha: \n"))
            if opcao == 1:
                pilha.push(input("Digite um nome para empilhar: "))
            elif opcao == 2:
                pilha.pop()
            elif opcao == 3:
                pilha.print_all()
            elif opcao == 4:
                pilha.print_top()
            elif opcao == 5:
                pilha.pop_all()
            elif opcao == 6:
                break
            else:
                print("Opção inválida.")

if __name__ == '__main__':
    Exercicio2.main()
