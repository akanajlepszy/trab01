import os

####### MENU PRINCIPAL #######


def menu():
    # Limpa a tela - Win/Linux
    # os.system('cls' if os.name == 'nt' else 'clear')
    print('\n..:: Gerenciamento ::..\n')
    print('1 - Registrar venda')
    print('2 - Repor estoque')
    print('3 - Mostrar Estoque')
    print('4 - Mostrar compras')
    print('5 - Maior compra')
    print('6 - Encerrar programa\n')
    item = input('Escolha uma opção: ')
    return item

####----DADOS DO CLIENTE----####


global nomeCliente
nomeCliente = ''

####--------ITEM UM------####

codigoIdUm = '1'
DescricaoUm = 'Calça'
global EstoqueUm
EstoqueUm = 20
ValorUm = 112.00

####--------ITEM DOIS------####

codigoIdDois = '2'
DescricaoDois = 'Camisa'
global EstoqueDois
EstoqueDois = 18
ValorDois = 95.00

####--------ITEM TRES------####

codigoIdTres = '3'
DescricaoTres = 'Bermuda'
global EstoqueTres
EstoqueTres = 23
ValorTres = 49.90

####--------ITEM QUATRO-----####

codigoIdQuatro = '4'
DescricaoQuatro = 'Saia'
global EstoqueQuatro
EstoqueQuatro = 12
ValorQuatro = 169.00

####--------ITEM CINCO------####

codigoIdCinco = '5'
DescricaoCinco = 'Blusa'
global EstoqueCinco
EstoqueCinco = 9
ValorCinco = 120.00

####--------ITEM SEIS------####

codigoIdSeis = '6'
DescricaoSeis = 'Moletom'
global EstoqueSeis
EstoqueSeis = 4
ValorSeis = 135.00

####--------ITEM SETE------####

codigoIdSete = '7'
DescricaoSete = 'Meia'
global EstoqueSete
EstoqueSete = 17
ValorSete = 12.99

####--------ITEM OITO------####

codigoIdOito = '8'
DescricaoOito = 'Tênis'
global EstoqueOito
EstoqueOito = 8
ValorOito = 183.00

####--------ITEM NOVE------####

codigoIdNove = '9'
DescricaoNove = 'Bota'
global EstoqueNove
EstoqueNove = 3
ValorNove = 219.90

#-------INICIO DE VARIAVEIS--------#

escolha = 0
codigoProduto = ''
global totalDeVendas
totalDeVendas = 0
global clienteMaiorCompra
clienteMaiorCompra = ''
global valorMaiorCompra
valorMaiorCompra = 0
global totalDeCompras
totalDeCompras = 0
global valorCompraUm
valorCompraUm = 0
global valorCompraDois
valorCompraDois = 0
global valorCompraTres
valorCompraTres = 0
global valorCompraQuatro
valorCompraQuatro = 0
global valorCompraCinco
valorCompraCinco = 0
global valorCompraSeis
valorCompraSeis = 0
global valorCompraSete
valorCompraSete = 0
global valorCompraOito
valorCompraOito = 0
global valorCompraNove
valorCompraNove = 0


def registra_compra(nomeCliente, descricao, estoque, valor, valorCompra, codigoProduto):
    quantidadeDeProdutos = int(input('Qual a quantidade de produtos? '))

    if quantidadeDeProdutos > estoque:
        print('\n{}, nosso estoque atual de {} é de {}, infelizmente não temos o estoque necessário'.format(
            nomeCliente, descricao, estoque))
    else:
        print('\n Olá {}, você escolheu o item {}'.format(
            nomeCliente, descricao))
        print('\n {}, nosso estoque atual de {}, é de {}, vamos prosseguir com sua compra!'.format(
            nomeCliente, descricao, estoque))
        valorCompra = quantidadeDeProdutos * valor
        confirmaCompra = input('\n {} o valor total de sua compra foi de R${:.2f}, podemos prosseguir (S/N)? '.format(
            nomeCliente, valorCompra))

        while confirmaCompra != 'S' or confirmaCompra != 'N':
            if confirmaCompra == 'S':
                estoque = estoque - quantidadeDeProdutos
                break
            elif confirmaCompra == 'N':
                break
            else:
                confirmaCompra = input(
                    '\n Não entendi a sua resposta, podemos prosseguir (S/N)? ')
    print(
        '\nDeseja mais alguma coisa, se sim por favor digite o código do produto, se não digite 0 para finalizar o atendimento.')

    set_vars(estoque, valorCompra, codigoProduto, nomeCliente)


def set_vars(estoque, valorCompra, codigoProduto, cliente):

    #-------PRODUTO UM-------#
    global nomeCliente
    nomeCliente = cliente

    if codigoProduto == '1':
        global EstoqueUm
        EstoqueUm = estoque
        global valorCompraUm
        valorCompraUm = valorCompra


#-------PRODUTO DOIS-------#

    elif codigoProduto == '2':
        global EstoqueDois
        EstoqueDois = estoque
        global valorCompraDois
        valorCompraDois = valorCompra

#-------PRODUTO TRES-------#

    elif codigoProduto == '3':
        global EstoqueTres
        EstoqueTres = estoque
        global valorCompraTres
        valorCompraTres = valorCompra

#-------PRODUTO QUATRO-------#

    elif codigoProduto == '4':
        global EstoqueQuatro
        EstoqueQuatro = estoque
        global valorCompraQuatro
        valorCompraQuatro = valorCompra

#-------PRODUTO CINCO-------#

    elif codigoProduto == '5':
        global EstoqueCinco
        EstoqueCinco = estoque
        global valorCompraCinco
        valorCompraCinco = valorCompra

#-------PRODUTO SEIS-------#

    elif codigoProduto == '6':
        global EstoqueSeis
        EstoqueSeis = estoque
        global valorCompraSeis
        valorCompraSeis = valorCompra

#-------PRODUTO SETE-------#

    elif codigoProduto == '7':
        global EstoqueSete
        EstoqueSete = estoque
        global valorCompraSete
        valorCompraSete = valorCompra

#-------PRODUTO OITO-------#

    elif codigoProduto == '8':
        global EstoqueOito
        EstoqueOito = estoque
        global valorCompraOito
        valorCompraOito = valorCompra

#-------PRODUTO NOVE-------#

    elif codigoProduto == '9':
        global EstoqueNove
        EstoqueNove = estoque
        global valorCompraNove
        valorCompraNove = valorCompra


def registrarVendas(codigoProduto):

    #-------INICIO DO REGISTRO DE VENDAS-------#
    global totalDeCompras
    global nomeCliente
    nomeCliente = input('Qual o nome do cliente? ')
    while codigoProduto != '0':
        codigoProduto = input('Qual o código do produto de 1 a 9? ')

#------------SAIR DE COMPRAS------------#

        if codigoProduto == '0':
            global totalDeCompras
            totalDeCompras = valorCompraUm + valorCompraDois + \
                valorCompraTres + valorCompraQuatro + valorCompraCinco + \
                valorCompraSeis + valorCompraSete + valorCompraOito + valorCompraNove
            maiorCompra()

            print('\nSaindo...')
            print(
                f'\nO total de compras de {nomeCliente} foi de R${totalDeCompras:.2f}')
            break

#------------PRODUTO UM------------#

        elif codigoProduto == codigoIdUm:
            registra_compra(nomeCliente, DescricaoUm, EstoqueUm,
                            ValorUm, valorCompraUm, codigoProduto)

#------------PRODUTO DOIS------------#

        elif codigoProduto == codigoIdDois:
            registra_compra(nomeCliente, DescricaoDois, EstoqueDois,
                            ValorDois, valorCompraDois, codigoProduto)

#------------PRODUTO TRES------------#

        elif codigoProduto == codigoIdTres:
            registra_compra(nomeCliente, DescricaoTres, EstoqueTres,
                            ValorTres, valorCompraTres, codigoProduto)

#------------PRODUTO QUATRO------------#

        elif codigoProduto == codigoIdQuatro:
            registra_compra(nomeCliente, DescricaoQuatro, EstoqueQuatro,
                            ValorQuatro, valorCompraQuatro, codigoProduto)

#------------PRODUTO CINCO------------#

        elif codigoProduto == codigoIdCinco:
            registra_compra(nomeCliente, DescricaoCinco, EstoqueCinco,
                            ValorCinco, valorCompraCinco, codigoProduto)

#------------PRODUTO SEIS------------#

        elif codigoProduto == codigoIdSeis:
            registra_compra(nomeCliente, DescricaoSeis, EstoqueSeis,
                            ValorSeis, valorCompraSeis, codigoProduto)

#------------PRODUTO SETE------------#

        elif codigoProduto == codigoIdSete:
            registra_compra(nomeCliente, DescricaoSete, EstoqueSete,
                            ValorSete, valorCompraSete, codigoProduto)

#------------PRODUTO OITO------------#

        elif codigoProduto == codigoIdOito:
            registra_compra(nomeCliente, DescricaoOito, EstoqueOito,
                            ValorOito, valorCompraOito, codigoProduto)

#------------PRODUTO NOVE------------#

        elif codigoProduto == codigoIdNove:
            registra_compra(nomeCliente, DescricaoNove, EstoqueNove,
                            ValorNove, valorCompraNove, codigoProduto)

        else:
            print('\nCodigo de produto invalido, digite novamente por favor: ')


def reporEstoque():
    ## ATUALIZA A VARIAVEL ESTOQUE ##
    print('1 - Calça\n2 - Camisa\n3 - Bermuda\n4 - Saia\n5 - Blusa\n6 - Moletom\n7 - Meia\n8 - Tenis\n9 - Bota')
    codigoProduto = input('Informe o cod do produto: ')
    while codigoProduto != '1' != '2' != '3' != '4' != '5' != '6' != '7' != '8' != '9':
        codigoProduto = input(
            'Nao existem produtos com o codigo informado, favor insira um código de 1 a 9: ')
    qtdProd = int(
        input('Informe a quantidade que deseja aumentar no estoque: '))

    if codigoProduto == 1:
        cliente = nomeCliente
        estoque = EstoqueUm + qtdProd
        valorCompra = 0
        print('Estoque do produto com codigo 1 atualizado.')
        print('Quantidade atualizada em estoque', estoque)
        set_vars(estoque, valorCompra, codigoProduto, cliente)

    elif codigoProduto == 2:
        cliente = nomeCliente
        estoque = EstoqueDois + qtdProd
        valorCompra = 0
        print('Estoque do produto com codigo 2 atualizado.')
        print('Quantidade atualizada em estoque', estoque)
        set_vars(estoque, valorCompra, codigoProduto, cliente)

    elif codigoProduto == 3:
        cliente = nomeCliente
        estoque = EstoqueTres + qtdProd
        valorCompra = 0
        print('Estoque do produto com codigo 3 atualizado.')
        print('Quantidade atualizada em estoque', estoque)
        set_vars(estoque, valorCompra, codigoProduto, cliente)

    elif codigoProduto == 4:
        cliente = nomeCliente
        estoque = EstoqueQuatro + qtdProd
        valorCompra = 0
        print('Estoque do produto com codigo 4 atualizado.')
        print('Quantidade atualizada em estoque', estoque)
        set_vars(estoque, valorCompra, codigoProduto, cliente)

    elif codigoProduto == 5:
        cliente = nomeCliente
        estoque = EstoqueCinco + qtdProd
        valorCompra = 0
        print('Estoque do produto com codigo 5 atualizado.')
        print('Quantidade atualizada em estoque', EstoqueCinco)
        set_vars(estoque, valorCompra, codigoProduto, cliente)

    elif codigoProduto == 6:
        cliente = nomeCliente
        estoque = EstoqueSeis + qtdProd
        valorCompra = 0
        print('Estoque do produto com codigo 6 atualizado.')
        print('Quantidade atualizada em estoque', estoque)
        set_vars(estoque, valorCompra, codigoProduto, cliente)

    elif codigoProduto == 7:
        cliente = nomeCliente
        estoque = EstoqueSete + qtdProd
        valorCompra = 0
        print('Estoque do produto com codigo 7 atualizado.')
        print('Quantidade atualizada em estoque', estoque)
        set_vars(estoque, valorCompra, codigoProduto, cliente)

    elif codigoProduto == 8:
        cliente = nomeCliente
        estoque = EstoqueOito + qtdProd
        valorCompra = 0
        print('Estoque do produto com codigo 8 atualizado.')
        print('Quantidade atualizada em estoque', estoque)
        set_vars(estoque, valorCompra, codigoProduto, cliente)

    elif codigoProduto == 9:
        cliente = nomeCliente
        estoque = EstoqueNove + qtdProd
        valorCompra = 0
        print('Estoque do produto com codigo 9 atualizado.')
        print('Quantidade atualizada em estoque', estoque)
        set_vars(estoque, valorCompra, codigoProduto, cliente)


def mostrarEstoque():
    ########## TABELA DE CONTROLE DE ESTOQUE DE TODOS OS PRODUTOS ############
    print('='*20, 'ESTOQUE', '='*20)
    x = 'N'
    while x != 'S':
        print('\nNome do produto: {}\nQuantidade em estoque: {}\nValor unitario: R$ {}\nValor total: R$ {}\n'.format(
            DescricaoUm, EstoqueUm, ValorUm, EstoqueUm*ValorUm))
        print('\nNome do produto: {}\nQuantidade em estoque: {}\nValor unitario: R$ {:.2f}\nValor total: R$ {:.2f}\n'.format(
            DescricaoDois, EstoqueDois, ValorDois, EstoqueDois*ValorDois))
        print('\nNome do produto: {}\nQuantidade em estoque: {}\nValor unitario: R$ {:.2f}\nValor total: R$ {:.2f}\n'.format(
            DescricaoTres, EstoqueTres, ValorTres, EstoqueTres*ValorTres))
        print('\nNome do produto: {}\nQuantidade em estoque: {}\nValor unitario: R$ {:.2f}\nValor total: R$ {:.2f}\n'.format(
            DescricaoQuatro, EstoqueQuatro, ValorQuatro, EstoqueQuatro*ValorQuatro))
        print('\nNome do produto: {}\nQuantidade em estoque: {}\nValor unitario: R$ {:.2f}\nValor total: R$ {:.2f}\n'.format(
            DescricaoCinco, EstoqueCinco, ValorCinco, EstoqueCinco*ValorCinco))
        print('\nNome do produto: {}\nQuantidade em estoque: {}\nValor unitario: R$ {:.2f}\nValor total: R$ {:.2f}\n'.format(
            DescricaoSeis, EstoqueSeis, ValorSeis, EstoqueSeis*ValorSeis))
        print('\nNome do produto: {}\nQuantidade em estoque: {}\nValor unitario: R$ {:.2f}\nValor total: R$ {:.2f}\n'.format(
            DescricaoSete, EstoqueSete, ValorSete, EstoqueSete*ValorSete))
        print('\nNome do produto: {}\nQuantidade em estoque: {}\nValor unitario: R$ {:.2f}\nValor total: R$ {:.2f}\n'.format(
            DescricaoOito, EstoqueOito, ValorOito, EstoqueOito*ValorOito))
        print('\nNome do produto: {}\nQuantidade em estoque: {}\nValor unitario: R$ {:.2f}\nValor total: R$ {:.2f}\n'.format(
            DescricaoNove, EstoqueNove, ValorNove, EstoqueNove*ValorNove))
        x = input('Deseja voltar ao menu principal(S/N)? ')


def mostrarCompra():
    x = 'N'
    while x != 'S':
        if EstoqueUm < 20:
            difEstoqueUm = 20 - EstoqueUm
            print('\nNome do produto: {}\nQuantidade vendida: {:.0f}\nValor unitario: R$ {}\nValor total vendido: R$ {}\n'.format(
                DescricaoUm, difEstoqueUm, ValorUm, ValorUm * difEstoqueUm))
        if EstoqueDois < 18:
            difEstoqueDois = 18 - EstoqueDois
            print('\nNome do produto: {}\nQuantidade vendida: {:.0f}\nValor unitario: R$ {}\nValor total vendido: R$ {}\n'.format(
                DescricaoDois, difEstoqueDois, ValorDois, ValorDois * difEstoqueDois))
        if EstoqueTres < 23:
            difEstoqueTres = 23 - EstoqueTres
            print('\nNome do produto: {}\nQuantidade vendida: {:.0f}\nValor unitario: R$ {}\nValor total vendido: R$ {}\n'.format(
                DescricaoTres, difEstoqueTres, ValorTres, ValorTres * difEstoqueTres))
        if EstoqueQuatro < 12:
            difEstoqueQuatro = 12 - EstoqueQuatro
            print('\nNome do produto: {}\nQuantidade vendida: {:.0f}\nValor unitario: R$ {}\nValor total vendido: R$ {}\n'.format(
                DescricaoQuatro, difEstoqueQuatro, ValorQuatro, ValorQuatro * difEstoqueQuatro))
        if EstoqueCinco < 9:
            difEstoqueCinco = 9 - EstoqueCinco
            print('\nNome do produto: {}\nQuantidade vendida: {:.0f}\nValor unitario: R$ {}\nValor total vendido: R$ {}\n'.format(
                DescricaoCinco, difEstoqueCinco, ValorCinco, ValorCinco * difEstoqueCinco))
        if EstoqueSeis < 4:
            difEstoqueSeis = 4 - EstoqueSeis
            print('\nNome do produto: {}\nQuantidade vendida: {:.0f}\nValor unitario: R$ {}\nValor total vendido: R$ {}\n'.format(
                DescricaoSeis, difEstoqueSeis, ValorSeis, ValorSeis * difEstoqueSeis))
        if EstoqueSete < 17:
            difEstoqueSete = 17 - EstoqueSete
            print('\nNome do produto: {}\nQuantidade vendida: {:.0f}\nValor unitario: R$ {}\nValor total vendido: R$ {}\n'.format(
                DescricaoSete, difEstoqueSete, ValorSete, ValorSete * EstoqueSete))
        if EstoqueOito < 8:
            difEstoqueOito = 8 - EstoqueOito
            print('\nNome do produto: {}\nQuantidade vendida: {:.0f}\nValor unitario: R$ {}\nValor total vendido: R$ {}\n'.format(
                DescricaoOito, difEstoqueOito, ValorOito, ValorOito * EstoqueOito))
        if EstoqueNove < 3:
            difEstoqueNove = 3 - EstoqueNove
            print('\nNome do produto: {}\nQuantidade vendida: {:.0f}\nValor unitario: R$ {}\nValor total vendido: R$ {}\n'.format(
                DescricaoNove, difEstoqueNove, ValorNove, ValorNove * EstoqueNove))
        print('\n Valor total vendido: R$ {}\n'.format(totalDeCompras))
        x = input('Deseja voltar ao menu principal(S/N)? ')


def maiorCompra():
    global valorMaiorCompra
    global clienteMaiorCompra
    global nomeCliente
    global totalDeCompras
    if totalDeCompras > valorMaiorCompra:
        valorMaiorCompra = totalDeCompras
        clienteMaiorCompra = nomeCliente
    return [clienteMaiorCompra, valorMaiorCompra]


# Processamento do menu e chamada das funções


while(escolha != '6'):
    escolha = menu()
    if escolha == '1':
        registrarVendas(codigoProduto)
    elif escolha == '2':
        reporEstoque()
    elif escolha == '3':
        mostrarEstoque()
    elif escolha == '4':
        mostrarCompra()
    elif escolha == '5':
        maiorCompra = maiorCompra()
        print(maiorCompra)
    elif escolha == '6':
        print('\nSaindo...\n')
    else:
        print('\nOpção desconhecida!\n')
        input('Pressione ENTER para continuar')
