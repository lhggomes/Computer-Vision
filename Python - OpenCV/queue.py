class fila:
    def __init__(self):
        self.fila =  []

    def inserir(self,n):
        self.fila.append(n)

    def excluir(self):
        del self.fila[0]


