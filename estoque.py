

class estoque:
    def __init__(self):
        self.listaPro = []
        pass
    def cadastro(self,nome, preco, tipo, quantidade,produtos):
        if len(self.listaPro) == 0:
            prod = produtos(nome, preco, tipo, quantidade)
            self.listaPro.append(prod)
            print '%d %s(s) cadastrado(s) com suceeso \n' % (prod.getQuantia(), prod.getNome())
        else:
            existente = False
            for i in range(len(self.listaPro)):
                if self.listaPro[i].getNome() == nome:
                    print '%s ja cadastrado no sistema \n'%nome
                    existente = True
                    break
            if existente == False:
                prod = produtos(nome, preco, tipo, quantidade)
                self.listaPro.append(prod)
                print '%d %s(s) cadastrado(s) com sucesso \n' % (prod.getQuantia(), prod.getNome())

    def vender(self,produto_ven):
        self.produto_ven = produto_ven
        return self.verificar(self.produto_ven)
    def verificar(self,produto_ven):
        total = 0
        existente = False
        teste = False
        for i in range(len(self.listaPro)):
            if self.listaPro[i].getNome() == produto_ven:
                print '==> %s (%s). R$%.2f'%(self.listaPro[i].getNome(),self.listaPro[i].getTipo(),self.listaPro[i].getPreco())
                quant = int(raw_input("Digite a quantidade que deseja vender: "))
                estoque = self.listaPro[i].getQuantia()
                teste = False
                if quant < 0:
                    print 'valor invalido \n'
                    teste = True
                    continue
                elif estoque < quant:
                    print 'Nao e possivel vender pois nao ha %s suficiente \n' % produto_ven
                else:
                    estoque -= quant
                    self.listaPro[i].setQuantia(estoque)
                    total = quant * self.listaPro[i].getPreco()
                    print '==> total arrecadado: R$ %.2f \n' % total
                existente = True
                break
        if existente == False and teste == False:
            print produto_ven + ' nao cadastrado(a) no sistema.'
        return total

    def impressao(self,total,total_geral):
        total_geral = 0.0
        for i in range(len(self.listaPro)):
            print '%d) %s (%s) R$ %2.f' % ((i+1),self.listaPro[i].getNome(), self.listaPro[i].getTipo(), self.listaPro[i].getPreco())
            print '   Restante: %d \n' % self.listaPro[i].getQuantia()
            total_geral += self.listaPro[i].getPreco() * self.listaPro[i].getQuantia()
        print 'Total arrecadado em vendas: R$ %.2f\n'%(total)
        print 'Total que pode ser arrecadado: R$ %.2f\n' % (total_geral)