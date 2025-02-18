


#Classe Mercadinho

#exibir os objetos:
def exibir_estoque():
    todos = Produtos.listar_produtos()
    for produtos in todos:
        print(f'Nome:{produtos.nome} Quantidade:{produtos.quantidade} Codigo:{produtos.codigo}')


class Produtos():

    todos_produtos = []

    def __init__(self,nome,quantidade,codigo):
        self._nome = nome
        self._codigo = codigo
        self._quantidade = quantidade
        self.tot_itens = 1
        Produtos.todos_produtos.append(self)

    @classmethod
    def listar_produtos(cls):
        return cls.todos_produtos

    @property
    def nome (self):
        return self._nome

    @nome.setter
    def nome(self,nome):
        self._nome = nome.title()
        self.tot_itens = self.tot_itens + 1

    @property
    def codigo(self):
        return self._codigo
    @codigo.setter
    def codigo(self,codigo):
        self._codigo = codigo

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self,quantidade):
        if quantidade < 0:
            raise ValueError("A Quantidade Nao pode ser Negativa")
        self._quantidade = quantidade

    def adicionar(self,valor):
        self._quantidade = self.quantidade + valor
        return print("Adicionado", valor)

    def retirar(self,valor):
        self._quantidade = self.quantidade - valor
        return print("Retirado", valor)

    def __repr__(self):
        return f"Nome:{self._nome} Quantidade:{self._quantidade} Codigo:{self._codigo}"


# quero fazer o app verificar itens iguais
    @classmethod
    def verificar(cls):
        print("-"*25)
        print("Verificando...")
        vistos = {}
        duplicados = []

        for produto in cls.listar_produtos():

            if produto.nome in vistos:
                vistos[produto.nome].quantidade += produto.quantidade
                duplicados.append(produto)
                print(f"{produto.nome} está Duplicado\n{produto.nome} Foi removido!\nQuantidade Adicionada ao Correlato!")
                print("Verifique Att em estoque!")
                print("-" * 25)
            else:
                vistos[produto.nome] = produto

        for produto in duplicados:
            cls.listar_produtos().remove(produto)
        print("Estoque Atualizado!")


p1 = Produtos(" ", 0,0)









