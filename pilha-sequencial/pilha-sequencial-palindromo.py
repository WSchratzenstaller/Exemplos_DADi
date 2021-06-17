class Minha_pilha: 
    def __init__(self):
        self.__pilha = []
 
    def push(self, nome):
        self.__pilha.append(nome)
 
    def pop(self):
        if self.__pilha:
            del self.__pilha[-1]
        else:
            print("Pilha vazia.")
 
    def inverter(self): 
        if self.__pilha:
            saida= "Pilha: \n"
            pilha_invertida=[]
            while self.__pilha:
                saida+= self.__pilha[-1]
                pilha_invertida.append(self.__pilha[-1])
                self.__pilha.pop()
            while pilha_invertida:
                self.__pilha.append(pilha_invertida[-1])
                del pilha_invertida[-1]
        else:
            print("Não há valores para imprimir.")
        return saida
 
    def palindromo(self):
        if self.__pilha:
            resultado_comparacao = "Falha ao comparar."
            palavra1= ""
            palavra2= ""
            pilha_invertida=[]
            while self.__pilha:
                palavra1+= self.__pilha[-1]
                pilha_invertida.append(self.__pilha[-1])
                del self.__pilha[-1]
            while pilha_invertida:
                palavra2+=pilha_invertida[-1]
                self.__pilha.append(pilha_invertida[-1])
                del pilha_invertida[-1]
            if palavra1 == palavra2:
                resultado_comparacao = "É palíndromo."
            else:
                resultado_comparacao = "Não é palíndromo."
        else:
            print("Não há valores para imprimir.")
        return resultado_comparacao

    def pop_all(self): 
        if self.__pilha:
            while self.__pilha:	
                del self.__pilha[-1] #poderia chamar self.__pilha.pop()
            print("Todos os valores foram excluidos.")
        else: 
            print("Não há valores para excluir.")
######
class Exercicio3:
    def main():
        pilha = Minha_pilha()
        while True:
            opcao = int(input("Opções:\n"
                              "1 – Incluir nova palavra/frase na pilha.\n"
                              "2 – Inverter e imprimir palavra/frase.\n"
                              "3 – Palindromo?\n"
                              "4 - Limpar pilha.\n"
                              "5 - Sair.\n"
                              "Escolha: \n"))
            if opcao == 1:
                palavra = input("Digite uma palavra/frase para empilhar: ")
                for letra in palavra:
                    pilha.push(letra)
            elif opcao == 2:
                desempilhada = pilha.inverter()
                print(desempilhada)
            elif opcao == 3:
                print(pilha.palindromo())
            elif opcao == 4:
                pilha.pop_all()
            elif opcao == 5:
                break
            else:
                print("Opção inválida.")

if __name__ == '__main__':
    Exercicio3.main()
