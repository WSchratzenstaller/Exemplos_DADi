from imovel import Imovel

class Novo(Imovel):
    def __init__(self, endereco, preco, adicional):
        super().__init__(endereco, preco)
        self.__adicional = adicional
        #self.__preco = (preco/100)*(100 + adicional) # preco próprio

    def get_adicional(self):
        return self.__adicional

    def imprime_adicional(self):
        print("Valor adicional: ", (super().get_preco()/100)*int(self.__adicional))