
global arquivo
arquivo = open('arquivo.txt', 'a+')
global Fcls


def add():
 txt = input("Digite o que deseja adicionar ao Arq de TXT: ")
 with open('arquivo.txt', 'a+', encoding='utf-8') as arquivo: # o 'a+' permite que o arquivo seja editavel e livel 'utf-8' faz aceitar acentuaçao
    arquivo.write(txt)
    arquivo.write('\n')

def limpar():
 Fcls = input("Tem Certeza que Deseja Limpar os Dados do Doc (S/N): ")
 if Fcls == 's':
     print("Limpando...")
     arquivo.close()
     limp = open('arquivo.txt' , 'w')
     limp.write('')
     limp.close()
 elif Fcls == 'n':
      print("Operação Cancelada!")


def exibir():
    arquivo.seek(0) #esse 'seek' é necessario para que o conteudo adicionado apareça
    conteudo = arquivo.read()
    print(conteudo)



op = int(input("1 - Adiconar Ao ARQ de TXT \n2 - Ler ARQ de TXT \n3- Apagar dados do ARQ de TXT \n  Valor: "))

match op:
   case 1:
      add()
   case 2:
      exibir()
   case 3:
      limpar()


              




    