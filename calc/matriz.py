import math


M2x2 =[ [0,0],
        [0,0] ]

M22x2 =[ [0,0],
         [0,0] ]

global a
global b
global c
global novo_valor
global sel 
global QuantM

def  CriadorM(Q):
   sel = 1
   a = 0
   b = 0
   c = 0
   def Mnum(H):
       if H == 1:
            M2x2[a][b] = novo_valor
       else: 
           M22x2[a][b] = novo_valor
   
   if Q == 1:
       contador = 4
   elif Q == 2:
       contador = 8
   
   while c < contador:
      if b == 2:
         a = a+1
         b = 0;
      if a == 2:
         a = 0
         b = 0;
         sel = 2
      
      novo_valor = float(input(print("digite o valor ", b+1, " da linha ", a+1," da Matriz 2x2:")))
      Mnum(sel)
      b= b+1
      c = c+1

def quant(K):
    match K:
       case '1': #Determinate
            CriadorM(1);
       case '2':
            CriadorM(2);


OP = input(" 1 - Determinate\n 2 - Transposta\n 3 - Igualdade de matrizes\n 4 -Adição de matrizes\n 5 - Subtração de matrizes\n 6 - Matriz oposta \n 7 - Hadamard Product \n 8 - Traço da Matriz \n 9 - Multiplicação de Matrizes \n 10 - Multiplicação de matriz por escalar\n Selecione a Operacao:")


match OP:
    case '1':
        QuantM = input("Uma ou Duas Matrizes: ")
        quant(QuantM)
        if QuantM == 1:
            Determinate = (M2x2[0][0]*M2x2[1][1])-(M2x2[0][1]*M2x2[1][0])
            print("\n \nO Valor do Determinante é: ", f"{Determinate:.1f}")
        else:
            Determinate = (M2x2[0][0]*M2x2[1][1])-(M2x2[0][1]*M2x2[1][0])
            DeterminateM2 = (M22x2[0][0]*M22x2[1][1])-(M22x2[0][1]*M22x2[1][0])
            print("\n \nO Valor do Determinante da M1 é: ", f"{Determinate:.1f}")
            print("\n \nO Valor do Determinante da M2 é: ", f"{DeterminateM2:.1f}");
    case '2':
        QuantM = input("Uma ou Duas Matrizes: ")
        quant(QuantM)
        if QuantM == 1: 
            print("\n \nA Transposta é:\n  [",M2x2[0][0] , ",", M2x2[1][0],"]\n", " [", M2x2[0][1],",",M2x2[1][1],"]" )
        else:
            print("\n \nA Transposta é:\n  [",M2x2[0][0] , ",", M2x2[1][0],"]\n", " [", M2x2[0][1],",",M2x2[1][1],"]" )
            print("\n \nA Transposta é:\n  [",M22x2[0][0] , ",", M22x2[1][0],"]\n", " [", M22x2[0][1],",",M22x2[1][1],"]" );
    case '3':
        quant('2')
        if M22x2[0][0] == M2x2[0][0] and M22x2[0][1] == M2x2[0][1] and M22x2[1][0] == M2x2[1][0] and M22x2[1][1] == M2x2[1][1]:
            print("\n \nAs Matrizes:\n  [",M2x2[0][0],",",M2x2[1][0],",", M22x2[0][0],",",M22x2[1][0],"]\n  [",M2x2[0][1],",",M2x2[1][1],",", M22x2[0][1],",",M22x2[1][1],"]\n \nSão Iguais\n" )
        else:
            print("\n \nAs Matrizes:\n  [",M2x2[0][0],",",M2x2[1][0],",", M22x2[0][0],",",M22x2[1][0],"]\n  [",M2x2[0][1],",",M2x2[1][1],",", M22x2[0][1],",",M22x2[1][1],"]\n \nNão São Iguais\n" );
    case '4':
            quant('2')
            print("\n \nA soma das Matrizes:\n  [",M2x2[0][0],",",M2x2[0][1],",", M22x2[0][0],",",M22x2[0][1],"]\n  [",M2x2[1][0],",",M2x2[1][1],",", M22x2[1][0],",",M22x2[1][1],"]\n \n É: \n \n  [",M2x2[0][0] + M22x2[0][0],",", M2x2[0][1] + M22x2[0][1],"]\n  [",M22x2[1][0] + M2x2[1][0],",", M2x2[1][1] + M22x2[1][1],"] ");
    case '5':
            quant('2')
            print("\n \nA Subtração das Matrizes:\n  [",M2x2[0][0],",",M2x2[0][1],",", M22x2[0][0],",",M22x2[0][1],"]\n  [",M2x2[1][0],",",M2x2[1][1],",", M22x2[1][0],",",M22x2[1][1],"]\n \n É: \n \n  [",M2x2[0][0] - M22x2[0][0],",", M2x2[0][1] - M22x2[0][1],"]\n  [",M22x2[1][0] - M2x2[1][0],",", M2x2[1][1] - M22x2[1][1],"] ");
    case '6':
            quant('1')
            print("\n \nA Inversa é:\n  [",(M2x2[0][0] * -1) , ",", M2x2[1][0] * -1,"]\n", " [", M2x2[0][1] * -1,",",M2x2[1][1] * -1,"]" );
    case '7':
            quant('2')
            print("\n \nO Hadamard Product de:\n  [",M2x2[0][0],",",M2x2[0][1],",", M22x2[0][0],",",M22x2[0][1],"]\n  [",M2x2[1][0],",",M2x2[1][1],",", M22x2[1][0],",",M22x2[1][1],"]\n \n É: \n\n [",M2x2[0][0] * M22x2[0][0],",", M2x2[0][1] * M22x2[0][1],"]\n[",M22x2[1][0] * M2x2[1][0],",", M2x2[1][1] * M22x2[1][1],"] ");
    case '8':
            quant('1')
            print("\n \nO Traço é:\n  [", M2x2[0][0] + M2x2[1][1], "]" );
    case '9':
            quant('2')
            print("\n \nA Multiplicação das Matrizes:\n  [",M2x2[0][0],",",M2x2[0][1],",", M22x2[0][0],",",M22x2[0][1],"]\n  [",M2x2[1][0],",",M2x2[1][1],",", M22x2[1][0],",",M22x2[1][1],"]\n \n É: \n \n  [",(M2x2[0][0] * M22x2[0][0])+(M2x2[0][1] * M22x2[1][0]) , ", ",(M2x2[0][0] * M22x2[0][1])+(M2x2[0][1] * M22x2[1][1]), "]\n [",(M2x2[1][0] * M22x2[0][0])+(M2x2[1][1] * M22x2[1][0]),",",(M2x2[1][0] * M22x2[0][1])+(M2x2[1][1] * M22x2[1][1]),"] ");
    case '10':
            quant('1')
            Esc = float(input("Defina o Escalar multiplicador: "))
            print("\n \n A Multiplicação por ", Esc, "É: \n\n [",M2x2[0][0] * Esc,",", M2x2[0][1] *  Esc,"]\n[",M2x2[1][0] *  Esc,",", M2x2[1][1] * Esc,"] ");

 



          








