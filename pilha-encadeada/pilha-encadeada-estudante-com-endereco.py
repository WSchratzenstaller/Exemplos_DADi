class No_pilha:
    def __init__(self):
        self.__nome = ""
        self.__cep = 0
        self.__numero = 0
        self.__complemento = ""
        self.__proximo = None

    def set_nome(self, nome):
        self.__nome = nome

    def set_cep(self, cep):
        self.__cep = cep
  
    def set_numero(self, numero):
        self.__numero = numero

    def set_complemento(self, complemento):
        self.__complemento = complemento

    def set_proximo(self, proximo):
        self.__proximo = proximo

    def get_nome(self):
        return self.__nome

    def get_cep(self):
        return self.__cep
 
    def get_numero(self):
        return self.__numero
    
    def get_complemento(self):
        return self.__complemento 

    def get_proximo(self):
        return self.__proximo
        
class Minha_pilha:
    def __init__(self):
        self.__topo = None

    def push(self, nome, cep, numero, complemento):
        temp = No_pilha()
        if temp:
            temp.set_nome(nome)
            temp.set_cep(cep)
            temp.set_numero(numero)
            temp.set_complemento(complemento)
            temp.set_proximo(self.__topo)
            self.__topo = temp

    def pop(self):
        if self.__topo:
            print("Estudante desempilhado:", self.__topo.get_nome())
            self.__topo = self.__topo.get_proximo()
        else:
            print("Nenhum cadastro para remover.")

    def print_all(self):
        temp = self.__topo
        saida = "Pilha de dados:\n"
        if self.__topo:
            while temp:
                saida += "Nome: " + temp.get_nome() + "\nCEP: " + str(temp.get_cep()) + "\nNúmero: " + str(temp.get_numero()) + "\nComplemento: " + temp.get_complemento() + "\n\n"
                temp = temp.get_proximo()
            print(saida)
        else:
            print("Nenhum cadastro para imprimir.")

class Prova1:
    def main():
        objeto_pilha = Minha_pilha()
        while True:
            op = int(input("Opcoes: \n"+
                           "1 - Empilhar.\n"+
                           "2 - Desempilhar.\n"
                           "3 - Imprimir pilha.\n"+
                           "4 - Sair.\n"))
            if op == 1:
                nome = input("Digite o nome:")
                cep = int(input("Digite o cep:"))
                numero = int(input("Digite o numero:"))
                complemento = input("Digite o complemento:")
                # Poderia instanciar um estudante:
                # - armazenar o estudante como objeto 
                # - e a indicação do próximo.
                objeto_pilha.push(nome, cep, numero, complemento)
            elif op == 2:
                objeto_pilha.pop()
            elif op ==3:
                objeto_pilha.print_all()
            elif op == 4:
                break
            else:
                print("Opcao invalida")

if __name__ == '__main__':
    Prova1.main()