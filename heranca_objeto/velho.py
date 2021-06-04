from imovel import Imovel

class Velho(Imovel):
    def __init__(self, endereco, preco, desconto):
        super().__init__(endereco, preco)
        self.__desconto = desconto
        #self.__preco = (preco/100)*(100 - desconto) # preco próprio

    def get_desconto(self):
        return self.__desconto

    def imprime_desconto(self):
        print("Valor do desconto: ", str(((super().get_preco()/100)*int(self.__desconto))))