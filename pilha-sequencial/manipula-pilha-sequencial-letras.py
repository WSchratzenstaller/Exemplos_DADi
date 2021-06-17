class Minha_pilha:
    def __init__(self): 
        self.__pilha=[]

    def push(self, letra):
        self.__pilha.append(letra)
        
    def pop(self):
        if self.__pilha:
            del self.__pilha[-1]
        else:
            print("Pilha vazia.")

    def print_all(self):
        guarda_pilha = []
        while self.__pilha:
            print(self.__pilha[-1])
            guarda_pilha.append(self.__pilha[-1])
            self.__pilha.pop()
        while guarda_pilha:
            self.__pilha.append(guarda_pilha[-1])
            guarda_pilha.pop()
        
    def print_top(self):
       print(self.__pilha[-1])
######################################################################## 
class Exemplo:
    def main():
        pilha = Minha_pilha()

        while True:
            op = int(input("1 – Empilhar letras.\n"+
                            "2 – Desempilhar (remove última letra/topo).\n"+
                            "3 – Imprimir tudo.\n"+
                            "4 – Imprimir topo.\n"+
                            "5 – Sair.\n"+
                            "Opcao: ")) 
            if op is 1:
                quantidade = (int(input("Quantas letras deseja empilhar?")))
                i=0
                while (i < quantidade):
                    pilha.push(input("Digite uma letra para empilhar: ")) 
                    i=i+1
            elif op is 2:
                pilha.pop()
            elif op is 3:
                pilha.print_all()
            elif op is 4:
                pilha.print_top()
            elif op is 5:
                break
            else:
                print("Opcao invalida.")

if __name__ == '__main__':
    Exemplo.main()