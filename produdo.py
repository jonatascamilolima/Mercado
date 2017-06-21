

class produtos:
    def __init__(self,nome,preco,tipo,quantidade):
        self.nome = nome
        self.preco = preco
        self.tipo = tipo
        self.quantidade = quantidade
    def getNome(self):
        return self.nome
    def getPreco(self):
        return self.preco
    def getTipo (self):
        return self.tipo
    def getQuantia(self):
        return self.quantidade
    def setQuantia(self,outro):
        self.quantidade = outro