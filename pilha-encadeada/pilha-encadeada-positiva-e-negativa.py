class No_pilha:
  def __init__(self):
    self.__valor = 0.0
    self.__proximo = None

  def set_valor(self, valor):
    self.__valor = valor
  
  def set_proximo(self, proximo):
    self.__proximo = proximo

  def get_valor(self):
    return self.__valor
  
  def get_proximo(self):
    return self.__proximo
        
class Pilha:
  def __init__(self):
    self.__topo = None

  def push(self, valor):
    temp = No_pilha()
    if temp:
        temp.set_valor(valor)
        temp.set_proximo(self.__topo)
        self.__topo = temp

  def pop(self):
     if self.__topo:
       print("Valor desempilhado:", self.__topo.get_valor())
       self.__topo = self.__topo.get_proximo()
     else:
       print("Nenhum cadastro encontrado.")

  def print_all(self):
    temp = self.__topo
    saida = 'Valores\n'
    if self.__topo:
      while temp:
        saida += str(temp.get_valor()) + '\n'
        temp = temp.get_proximo()
      print(saida)
    else:
      print("Nenhum cadastro encontrado.")

  def get_topo(self):
    return self.__topo

class Exercicio6:
  def main():
    pilha_positiva = Pilha()
    pilha_negativa = Pilha()
    while True:
      op = int(input("Opcoes: \n"+
                     "1 Empilhar.\n"+
                     "2 Imprimir pilhas.\n"+
                     "3 Sair.\n"))
      if op == 1:
        valor = int(input("Digite a valor:"))
        if valor > 0:
          pilha_positiva.push(valor)
        elif valor < 0:
          pilha_negativa.push(valor)
        else:
          pilha_positiva.pop()
          pilha_negativa.pop()
      elif op == 2:
          op2 = int(input("Qual pilha deseja imprimir? \n"+
                          "1 Positiva.\n"+
                          "2 Negativa.\n"+
                          "3 Ambas.\n"+
                          "4 Voltar.\n"))
          if op2 == 1:
            print("Pilha Positiva")
            pilha_positiva.print_all()
          elif op2 == 2:
            print("Pilha Negativa")
            pilha_negativa.print_all()
          elif op2 == 3:
            pilha_todos = Pilha()
            temp = pilha_positiva.get_topo()
            if temp:
              while temp:
                pilha_todos.push(temp.get_valor())
                temp = temp.get_proximo()
            temp = pilha_negativa.get_topo()
            if temp:
              while temp:
                pilha_todos.push(temp.get_valor())
                temp = temp.get_proximo()
              temp = pilha_positiva.get_topo()
            pilha_todos.print_all()
          elif op2 == 4:
            exit()
          else:
            print("Opcao invalida")
      elif op == 3:
        break
      else:
        print("Opcao invalida")

if __name__ == '__main__':
  Exercicio6.main()