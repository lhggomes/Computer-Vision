class Fila:
    def __init__(self):
        self.fila =  []

    def inserir(self,n):
        self.fila.append(n)
    #A Funcção de inserçao utlizrá o append

    def excluir(self):
        if not self.vazia():
          return self.fila.pop(0)


    def tamanho(self):
        return len(self.fila)

    def vazia(self):
        return self.tamanho()== 0



fila = Fila()
fila.vazia()

fila.inserir(1)
fila.inserir(2)
fila.inserir(3)
fila.excluir()

print(fila.tamanho())
print(fila.vazia())

