import datetime

class Pessoa:
    def __init__(self, nome, nascimento, cpf):
        self.__nome = nome
        self.__nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')
        self.__cpf = cpf

    def set_nome(self, nome):
        self.__nome = nome
    
    def set_nascimento(self, nascimento):
        self.__nascimento = nascimento

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_nome(self):
        return self.__nome
    
    def get_nascimento(self):
        return self.__nascimento

    def get_cpf(self):
        return self.__cpf
############################################
def main():
    operacao = 0
    lista = []

    while True:
        operacao = int(input("Opções:\n"
                             "1 - Adicionar nova pessoa.\n"
                             "2 - Imprimir lista de pessoas.\n"
                             "3 - Ordenar pessoas por data de nascimento.\n"
                             "4 - Sair.\n"))

        if operacao == 1:
            nome = input("Informe o nome da pessoa: \n")
            nascimento = input("Informe o nascimento do(a) " + nome + "\n")
            cpf = input("Informe o CPF do(a) " + nome + "\n")

            objetoPessoa = Pessoa(nome, nascimento, cpf)
            lista.append(objetoPessoa)
            
            ### 
            # Para inserir pessoas automaticamente 
            #    replique o bloco de código comentado
            #    descomente-o e altere os valores.
            # Lembre de comentar o bloco anterior, pois
            #    ele seguirá solicitando os dados para inserção.
            #nome = "Maria"
            #nascimento = "19/01/1921"
            #cpf = 1
            #lista.append(Pessoa(nome, nascimento, cpf)) 
            ###

        elif operacao == 2:
            for pessoa in lista:
                pessoa_nascimento = '{}/{}/{}'.format(pessoa.get_nascimento().day, pessoa.get_nascimento().month, pessoa.get_nascimento().year)
                print(pessoa.get_nome() + " - " + pessoa_nascimento + " - " + str(pessoa.get_cpf()))
        
        elif operacao == 3:
            n = len(lista)-1
            for i in range(n, 0, -1):
                for j in range(n):
                    if lista[j].get_nascimento() > lista[j + 1].get_nascimento():
                        auxiliar = lista[j]
                        lista[j] = lista[j + 1]
                        lista[j + 1] = auxiliar
        elif operacao == 4:
            break
        else:
            print("Informe uma operação válida.")

if __name__ == '__main__':
    main()
