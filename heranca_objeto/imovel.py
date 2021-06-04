class Imovel():
    def __init__(self, endereco, preco):
        self.__endereco = endereco
        self.__preco = preco

    def set_endereco(self, endereco):
        self.__endereco = endereco

    def get_endereco(self):
        return self.__endereco

    def set_preco(self, preco):
        self.__preco = preco

    def get_preco(self):
        return self.__preco