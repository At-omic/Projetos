from classe_M import Produtos, exibir_estoque
#na classe_M existe um objeto inicial "p1 = Produtos(" ", 0,0)"
while True:

    print("1 - Add Item\n2 - Remover Item\n3 - Att Item\n4 - Ver Estoque\n5 - Verificar Dualidades\n6- Sair")
    print("-" * 25)
    op = int(input("Opção:"))


    match op:
        case 1:
            for produto in Produtos.listar_produtos():
                a = 1
            novo_OBJ_nome = input("Nome:")
            novo_OBJ_quantidade = int(input("Quantidade:"))
            novo_OBJ_codigo = produto.codigo + 1
            novo_OBJ = Produtos(novo_OBJ_nome,novo_OBJ_quantidade,novo_OBJ_codigo)
            print(f"{novo_OBJ_nome} Foi Add, Codigo do Produto: {novo_OBJ_codigo}")
            print('-' * 25)
        case 2:
            encontrado = False
            procurador = int(input("Digite o codigo do produto:"))
            for produtos in Produtos.listar_produtos():
                if produtos.codigo == procurador and produtos.codigo > 0:
                    op_sn = input(f"{produtos.nome} Foi Selecionado e será removido. confirma (s/n)?")
                    if op_sn.lower() == 's':
                        Produtos.listar_produtos().remove(produtos)
                        print(f'{produtos.nome} Excluido!')
                        print("-" * 25)
                    else:
                        print("Operação Finalizada!")
                        print("-" * 25)

                    encontrado = True
                    break
            if not encontrado :
                print(f'Codigo {procurador} Não foi encontrado!')
                print("-" * 25)

        case 3:
            procurador = int(input("Digite o codigo do produto:"))
            existe = False
            for produtos in Produtos.listar_produtos():
                if produtos.codigo == procurador:
                    print("Produto: ", produtos.nome,"\n\n1 - Att Nome do Produto\n2 - Att Quantidade do Produto\n3 - Sair")
                    print("-" * 25)
                    op_att = int(input("Opção:"))
                    match op_att:
                        case 1:
                            novo_nome = input("Novo Nome:")
                            print(produtos.nome," Foi Att Para:",novo_nome)
                            produtos.nome = novo_nome
                            print("-" * 25)
                        case 2:
                            nova_quantidade = int(input(f"Quantidade Atual:{produtos.quantidade}\nDigite a Nova Quantidade:"))
                            print(produtos.quantidade, " Foi Att Para:", nova_quantidade)
                            produtos.quantidade = nova_quantidade
                            print("-" * 25)
                        case 3:
                            print("Operação Finalizada!")
                            print("-" * 25)
                            break
                        case _:
                            print("Opção Inválida!")
                            print("-" * 25)
                    existe = True
                    break
            if not existe: print(f"Codigo {procurador} Não Foi Encontrado!")


        case 4:
            exibir_estoque()
            print("-" * 25)

        case 5:
            Produtos.verificar()

        case 6:
            print("Saindo...")
            break