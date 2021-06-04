from novo import Novo
from velho import Velho

class Principal:
    def main():
        imoveis_novos = []
        imoveis_velhos = []
        while True:
            operacao = int(input("Opções:\n"
                                "1 - Adicionar imóvel.\n"
                                "2 - Imprimir lista de imóveis.\n"
                                "3 - Sair.\n"))

            if operacao == 1:
                endereco = input("Informe o endereço do imóvel:\n")
                preco = float(input("Informe o preço do imóvel:\n"))
                tipo = input("Informe N para imóvel Novo e V para Velho:\n")
                ###
                # Para gerar 10 imoveis automaticamente descomente o bloco e idente a parte seguinte
                # Também pode comentar as linhas que pedem os valores adicional e desconto.
                for i in range(0, 10):
                    endereco = "Endereco" + str(i)
                    preco = 100
                    adicional = desconto = (10+i)
                    if i%2==0:
                        tipo = "N"
                    else:
                        tipo = "V"
                ###
                    if tipo == "N":
                        #adicional = input("Informe a porcentagem adicional do valor:\n")
                        objeto_novo = Novo(endereco, preco, adicional)
                        imoveis_novos.append(objeto_novo)
                    elif tipo == "V":
                        #desconto = input("Informe a porcentagem do desconto:\n")
                        objeto_velho = Velho(endereco, preco, desconto)
                        imoveis_velhos.append(objeto_velho)
                    else:
                        print("Opção inválida.")

            elif operacao == 2:
                tipo = input("Que lista deseja imprimir?\n"
                             "N = Imóveis novos.\n"
                             "V = Imóveis velhos.\n"
                             "T = Todos os imóveis.\n")
                # Para evitar repetição de código e manter mais organizado, poderiamos definir métodos para impressão.
                tipo = tipo.upper()
                if tipo == "N":
                    for imovel in imoveis_novos:
                        preco_atual = (imovel.get_preco()/100)*(100 + int(imovel.get_adicional()))
                        print("Endereço: ",imovel.get_endereco(), 
                              "Preço de venda: ", str(preco_atual))
                        imovel.imprime_adicional()
                elif tipo == "V":
                    for imovel in imoveis_velhos:
                        print("Endereço: " + imovel.get_endereco(), 
                              "Preço de venda: " + str((imovel.get_preco()/100)*(100 - int(imovel.get_desconto()))))
                        imovel.imprime_desconto()
                elif tipo == "T":
                    for imovel in imoveis_novos:
                        preco_atual = (imovel.get_preco()/100)*(100 + int(imovel.get_adicional()))
                        print("Endereço: ",imovel.get_endereco(), 
                              "Preço de venda: ", str(preco_atual))
                        imovel.imprime_adicional()
                    for imovel in imoveis_velhos:
                        print("Endereço: " + imovel.get_endereco(), 
                              "Preço de venda: " + str((imovel.get_preco()/100)*(100 - int(imovel.get_desconto()))))
                        imovel.imprime_desconto()
                else:
                    print("Opção inválida.")
            elif operacao == 3:
                break
            else:
                print("Informe uma operação válida.")


if __name__ == '__main__':
    Principal.main()