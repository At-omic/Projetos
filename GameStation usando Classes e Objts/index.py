from GameStation_clientes import Cliente
from GameStation_clientes import crianca


#Aqui sera o cadastro de usuarios: ----  Dá para conectar com o Banco de Dados Local que criei com matrizes.


cliente1 = Cliente("victor",24,1,0)
crianca1 = crianca("joao",11,2,0,3)

cliente1.detalhes()
crianca1.detalhes()

#cliente1.carregar_cartao(10)
#crianca1.carregar_cartao(150)

#cliente1.gastar(5)
#crianca1.gastar(2)