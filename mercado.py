from produdo import produtos
from estoque import estoque
totalBalanco = 0.0
total_geral = 0.0111
estoque = estoque()
while True:
    print "\n = = = = Bemvindo(a) ao EconomizaTec= = = = \n"
    print "Digite a opcao desejada:\n"
    print "Cadastrar um Produto: 1"
    print "Vender um Produto: 2"
    print "Imprimir Balanco: 3"
    print "Sair: 4\n"

    try:
        opcao = int(raw_input("Opcao: "))
    except:
        print 'Valor invalido, tente novamente'
        continue

    if opcao == 1:
        while True:
            print "\n = = = = Cadastro de Produtos = = = = \n"
            nome = raw_input("Digite o nome do produto: ")
            try:
                preco = float(raw_input("Digite o Preco unitario do produto: "))
                if preco <= 0:
                    print '\nValor invalido\n'
                    continue
            except:
                print '\nValor invalido, tente novamente\n'
                continue
            tipo = raw_input("Digite o tipo do produto: ")
            try:
                quantidade = int(raw_input("Digite a quantidade do produto: "))
                if quantidade <= 0:
                    print 'Valor invalido'
                    continue
            except:
                print 'Valor invalido, tente novamente'
                continue

            estoque.cadastro(nome,preco,tipo,quantidade,produtos)

            novo_cadastro = raw_input("Deseja cadastrar outro produto? sim/nao ")
            if novo_cadastro.upper() == "SIM":
                continue
            elif novo_cadastro.upper() == "NAO":
                break

    if opcao == 2:
        while True:
            print "\n= = = = Venda de Produtos = = = = \n"
            nome_p = raw_input('Digite o nome do produto: ')
            totalBalanco += estoque.verificar(nome_p)
            op_venda = raw_input('Deseja vender outro produto? : ')
            if op_venda.upper() == "SIM":
                continue
            else:
                break

    if opcao == 3:
        while True:
            print "= = = = Impressao de Balanco = = = = \n"
            print "Produtos cadastrados: \n"
            estoque.impressao(totalBalanco,total_geral)
            nova_consulta = raw_input('Deseja realizar outra consulta ?')
            if nova_consulta.upper() == 'SIM':
                continue
            else:
                break

    elif opcao == 4:
        break
    elif opcao not in (1,2,3,4):
        print 'Valor invalido, tente novamente'
        continue