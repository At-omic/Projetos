
#sistema de crédito, vamos supor que vai funcionar como o GameStation onde o cliente Compra o Crédito no balcão e usa na loja.

class Cliente:
    def __init__(self,nome,idade,codliente,saldo):
       self.nome = nome
       self.idade = idade
       self.codliente = codliente
       self.saldo = saldo
 
    def detalhes(self):
        #print("\n")
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)
        print("Saldo: ", self.saldo)
        print("Código do Cliente: ", self.codliente)
        print("\n")

    def gastar(self,custo):
        self.custo = custo
        print(self.nome, "Gastou ",self.custo," Créditos")
        self.saldo = self.saldo - self.custo

    def creditar(self,valor):
        self.credito = valor
        self.saldo = self.saldo + self.credito

    # Aqui o limitador vai contar e informar quantos creditos a crianca tem e o limite, adicionando o devido e devolvendo o excesso

    def carregar_cartao(self,valor):
        if self.idade >= 18:
            cliente1.creditar(valor)
            print(self.nome, "ADD:", valor, " Créditos")
        else:
            match self.seguranca:
                case 1:
                    if self.saldo < 10:
                        Valoradd = 10 - self.saldo
                        t = valor + self.saldo
                        if t > 10: print("Limite: 10 Créditos\n ADD:",Valoradd," Créditos\n Devolvido:", (valor - Valoradd),"Créditos")
                        elif t <= 10:
                            print(self.nome, "ADD:", valor, " Créditos")
                            crianca1.creditar(valor)
                case 2:
                    if self.saldo < 20:
                        Valoradd = 20 - self.saldo
                        t = valor + self.saldo
                        if t > 20: print("Limite: 20 Créditos\n ADD:",Valoradd," Créditos\n Devolvido:", (valor - Valoradd),"Créditos")
                        elif t <= 20:
                            print(self.nome, "ADD:", valor, " Créditos")
                            crianca1.creditar(valor)
                case 3:
                    if self.saldo < 30:
                        Valoradd = 30 - self.saldo
                        t = valor + self.saldo
                        if t > 30: print("Limite: 30 Créditos\n ADD:",Valoradd," Créditos\n Devolvido:", (valor - Valoradd),"Créditos")
                        elif t <= 30:
                            print(self.nome, "ADD:", valor, " Créditos")
                            crianca1.creditar(valor)


#vou usar a parte de herança para criar clientes crianças, que nao terao acesso a todos os brinquedo e limite de credito ( 1 - ate 10 2 - ate 20 3 - ate 30 )

class crianca(Cliente):
    def __init__(self,nome,idade,codliente,saldo,seguranca):
     super().__init__(nome,idade,codliente,saldo)
     self.seguranca = seguranca


