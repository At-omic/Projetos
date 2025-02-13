import math
verde = "\033[92m"
reset = "\033[0m"  # Para resetar as cores

print(f"{verde}Para Operações Matemáticas Básicas e Avançadas Use:.{reset}\n\n1. **Soma**\n2. **Subtração**\n3. **Multiplicação**\n4. **Divisão**\n5. **Potenciação**\n6. **Radiciação (Raiz Quadrada, Raiz Cúbica, etc.)**\n7. **Exponencial (e^x)**\n8. **Módulo**\n9. **Divisão Inteira**\n10. **Conversão de Graus para Radianos**\n11. **Conversão de Radianos para Graus**\n12. **Cálculo de Hipotenusa**\n13. **Arredondamento (round)**\n14. **Arredondamento para Cima (ceil)**\n15. **Arredondamento para Baixo (floor)**\n16. **Maior/Menor de Dois Números (max/min)**\n17. **Cálculo da Distância Entre Dois Pontos**\n18. **Cálculo de Determinante de Matriz 2x2**\n19. **Solução de Equação de Primeiro Grau**\n")
print(f"{verde}Para  Operações de Cálculo Geométrico Use:.{reset}\n\n20. **Cálculo de Área e Perímetro de Retângulo**\n21. **Cálculo de Área e Perímetro (Circunferência) de Círculo**\n22. **Verificação de Triângulo (Desigualdade Triangular)**")
print(f"{verde}Para Operações de Análise Numérica e Financeira Use:.{reset}\n\n23. **Verificação de Números Primos**\n24. **Conversor de Unidades (Milhas para Quilômetros, Metros para Pés, etc.)**\n25. **Calculadora de Juros Simples**\n26. **Calculadora de Juros Compostos**\n27. **Soma de Números Naturais (usando Recursão)**\n28. **Fatorial de um Número (usando Recursão)**\n29. **Permutação**\n30. **Combinação**\n31. **Conversor de Bases Numéricas (Decimal para Binário, Hexadecimal, etc.)** \n32. **Cálculo de Média**\n33. **Cálculo de Desvio Padrão**\n34. **Calcular Tangente de uma Reta Dados os Coeficientes**")



















def conversor(Va1,tipo,txt):
    resto = []
    Cont_Resto = 0
    while Va1 > 1:
        math.trunc(Va1)%tipo
        Hbin = math.trunc(Va1)%tipo
        if Hbin <= 9:
                    resto.append(math.trunc(Va1)% tipo);
        else:
                    match Hbin:
                        case 10:
                            resto.append('A')
                        case 11:
                            resto.append('B')
                        case 12:
                            resto.append('C')
                        case 13:
                            resto.append('D')
                        case 14:
                            resto.append('E')
                        case 15:
                            resto.append('F')
        Va1 = Va1/tipo
        Va1 = math.trunc(Va1)
        Cont_Resto = Cont_Resto + 1;

    resto.append(math.trunc(Va1)%tipo)
    print(Va, txt ,"(",end='')
    for x in resto[::-1]:
            print(x, end='');
    print(")")
    resto.clear()


def media(Tot_num):
        global Resultado_Media
        global cesta
        cesta = []
        Div = Tot_num
        while Tot_num != 0:
            #print(Tot_num)
            cesta.append(float(input("Valor:")))
            Tot_num = Tot_num -1
        
        Resultado_Media= sum(cesta)/Div




def simplificador(Va,Di):
    global SVa
    global SDi
    while ((Va % 2) == 0 and (Di % 2) == 0) or ((Va % 3) == 0 and (Di % 3) == 0) or ((Va % 4) == 0 and (Di % 4) == 0) or ((Va % 5) == 0 and (Di % 5) == 0) or  ((Va % 6) == 0 and (Di % 6) == 0) or ((Va % 7) == 0 and (Di % 7) == 0) or ((Va % 8) == 0 and (Di % 8) == 0) or ((Va % 9) == 0 and (Di % 9) == 0)  :
            for c in range(2,9):
                    if (Va % c) == 0 and (Di % c) == 0:
                        Va = Va/c
                        Di = Di/c;
    SVa = Va
    SDi = Di;      
 

def recusao1(n):
            if n <=1:
                return n
            else:
                return n * recusao1(n-1)

op = int(input(f"{verde}Informe a operação:{reset}"))

if op == 9:
    Va = int(input("Primeiro Valor:"))
    Vb = int( input("Segundo Valor:"))

elif op == 8: 
    Va = float(input("Primeiro Valor:"))

elif op == 10: 
    Va = int(input("Graus: "));

elif op == 11: 
    Va = float(input("Dividendo: "))
    Vb = float( input("Divisor: "))

elif op == 1 or op ==2 or op == 3 or op == 4 or op == 5 or op ==6 or op == 7 or op == 16:
    Va = float(input("Primeiro Valor:"))
    Vb = float( input("Segundo Valor:"));

elif op == 13 or op == 15 or op == 14:
    x = float( input("Digite o Valor a ser arredondado: "));



match op: 
   case 1: Resultado = (Va+Vb)           #soma
   case 2: Resultado = (Va-Vb)           #Subtracao
   case 3: Resultado = (Va*Vb)           #Multiplicao
   case 4: Resultado = (Va/Vb)           #Divisao
   case 5: Resultado = (Va**Vb)          #Potencia
   case 6: Resultado = (Va**(1/Vb))      #Raiz
   case 7: Resultado = (Va**Vb)          #Exponencial
   case 8: 
          if Va > 0 : 
            Resultado = (Va) 
          else:  
            Resultado = (Va * -1)                                                                                #Modulo
   case 9: Resultado = math.floor(Va/Vb)                                                                         #Divisao Int
   case 10:                                                                                                      #Grau para Rad 
        
        simplificador(Va,180);
        print("Resultado: (", SVa, "/", SDi, ")  π Radianos" )
             
   case 11:                                                                                                      #Rad para Grau 
        sel = 0
        sel = input("Digite:  1 para π Radianos  e  2  para Radianos: ")
        match sel:
            case '1': 
                print("(", Va,"/", Vb, ") π Radianos")
                Va = Va * 180
                simplificador(Va,Vb)
                if ( SVa%SDi ) == 0:
                     print("Resultado: " , (SVa/ SDi) , "  Graus" );
                else:
                     print("Resultado: (", SVa, "/", SDi, ")  Graus" );
            
            case '2':
                print("(", Va,"/", Vb, ") Radianos")
                Va = Va * 57.32484076433121
                if  Vb > 1:
                     print("Resultado: (",f"{Va:.0f}", "/", f"{Vb:.0f}", ")  Graus" );
                else:
                    print("Resultado:" ,f"{Va:.0f}", "  Graus" );

match op:
     case 12:                                                                                                    #Cálculo de Hipotenusa
       Co =  float(input("Cateto Oposto: "))
       Ca =  float(input("Cateto Adjacente: "))
       print("Hipoternusa : ", (((Co **2)+(Ca**2))**(1/2)) );
    
     case 13:                                                                                                    #Arredondamento
        x = round(x)
        print("Resultado: ", x)
     case 14:                                                                                                    #Arredondamento + 
        x = math.ceil(x)
        print("Resultado: ", x);
     case 15:                                                                                                    #Arredondamento - 
        x = math.floor(x)
        print("Resultado: ", x)
     case 16:                                                                                                    #Maior/Menor de Dois Números
        if Va>Vb:
            print(Va, " é maior que ",Vb)
        else:
            print(Vb, " é maior que ",Va);
     case 17:                                                                                                    #Cálculo da Distância Entre Dois Pontos
        Pa = float(input("Digite a posicao do ponto 1: "))
        Pb = float(input("Digite a posicao do ponto 2: "))
        if Pa>Pb:
            print(Pa, " esta a ", Pa-Pb, " pontos de distancia de ",Pb)
        else:
            print(Pa, " esta a ", Pb-Pa, " pontos de distancia de ",Pb);
     case 18:                                                                                                    #Cálculo de Determinante de Matriz 2x2
        a = 0
        b = 0
        c = 0
        M2x2 =[ [0,0],
                [0,0] ]
        while c < 4:
            
            if b == 2:
                a = a+1
                b = 0;
            novo_valor = float(input(print("digite o valor ", b+1, " da linha ", a+1," da Matriz 2x2: ")))
            M2x2[a][b] = novo_valor
            b= b+1
            c = c+1
        Determinate = (M2x2[0][0]*M2x2[1][1])-(M2x2[0][1]*M2x2[1][0])
        print("O Valor do Determinante é: ", f"{Determinate:.1f}");
     case 19:                                                                                                    #Solução de Equação de Segundo Grau
        a = float(input("Digite o Valor do A em AX²: "))
        b = float(input("Digite o Valor do B em Bx: "))
        c = float(input("Digite o Valor do C: "))
        delta = ((b**2)-((4*a)*c))
        if delta > 0:
            x1= (((b *-1) + (delta)**(1/2))) /2*a
            x2= (((b *-1) - (delta)**(1/2))) /2*a
            print("Resultado: X1 = ", f"{x1:.2f}", " X2= ", f"{x2:.2f}")
        elif delta == 0:
            x1= (((b *-1) + (delta)**(1/2))) /2*a
            print("Resultado: X1 e X2 = ",x1)
        else:
            print(a,"X²+",b,'X +',c, " Nao Possui Raízes Reais, Delta = ", delta);

                                                                                                                # Operações de Cálculo Geométrico



     case 20:                                                                                                    #Cálculo de Área e Perímetro de Retângulo
        B = float(input("Digite o tamanho da Base: "))
        h = float(input("Digite o tamanho da Lateral: "))
        area = (B*h)/2
        perimetro = 2*B + 2*h
        print(" Área:", f"{area:.2f}", " Perímetro: ", f"{perimetro:.2f}");
    
     case 21:                                                                                                   #Cálculo de Área e Perímetro de Círculo
        A = float(input("Digite o Valor do Raio da Circunferência: "))
        Area = 3.14*(A**2)
        Peri = 2*3.14*A
        print(" Área:", f"{Area:.2f}", " Perímetro: ", f"{Peri:.2f}");
     case 22:                                                                                                   #Verificação de Triângulo (Desigualdade Triangular)
        a = float(input("Digite o Valor do Lado a: "))
        b = float(input("Digite o Valor do Lado b: "))
        c = float(input("Digite o Valor do Lado c: "))
        if a > b+c or b > a+c or c > a+b:
            print("Utilizando,",a,b,c,", Não é possível criar um triângulo.")
        else:
            print("Utilizando,",a,b,c,", é possível criar um triângulo.")


                                                                                                                # Operações de Análise Numérica e Financeira

     case 23:                                                                                                   #Verificação de Números Primos
        Va = float(input("Digite um Número: "))
        c = 0
        Divisores = 0
        while c <= Va:
                c = c+1
                if (Va % c) == 0:
                    print("Divisor: ", c)
                    Divisores = Divisores +1;
        if Divisores == 2:
                print(f"{Va:.0f}", " È um Número Primo!");
        else:
                print( f"{Va:.0f}", " Não é um Número primo.");
     case 24:                                                                                                   #Conversor de Unidades (Milhas para Quilômetros, Metros para Pés, etc.)
        Vb = int(input("Selecione a unidade de medida:\n Use:\n 1 para Área\n 2 para Comprimento\n 3 para Velocidade Angular\n Selecionar: " ))
        Va = float(input("Digite o Valor: "))
        match Vb:
            case 1:
                print("are: ", (Va*0.01))
                print("acre: ", (Va*0.0002471053))
                print("centímetro quadrado: ", (Va*10000))
                print("pé quadrado (square foot): ", (Va*10.76426264))
                print("hectare: ", (Va*0.0001))
                print("polegada quadrada (square inch): ", (Va*1549.907005 ))
                print("quilómetro quadrado	: ", (Va*0.000001))
                print("milímetro quadrado: ", (Va*1000000))
                print("jarda quadrada: ", (Va*1.19598939404))
            case 2:
                print("centímetros: ",Va* 100 )
                print("quilómetro: ",Va* 0.001)
                print("pés (foot)",Va* 3.28083 )
                print("polegada (inch)",Va*39.37007  )
                print("milha",Va* 0.000621371192)
                print("milha nautica",Va*0.000539957 )
                print("milímetro",Va*1000  )
                print("jarda",Va* 0.000621371192)
            case 3:
                print("herz",Va*0.159154943 )
                print("Radianos por segundo",Va*9.54929658 );
     case 25:                                                                                                    #Calculadora de Juros Simples
        Va= float(input("Valor inicial: "))
        i= float(input("Taxa ao Mês: "))
        T= float(input("Tempo Investido:  "))
        Capital = (Va*T*i)/100
        print("Montante Após", f"{T:.0f}","Meses: ", Capital+Va);
     case 26:                                                                                                    #Calculadora de Juros Compostos
        Va= float(input("Valor inicial: "))
        i= (float(input("Taxa ao Mês: ")))/100
        T= float(input("Tempo Investido:  "))
        print(i)
        Capital = Va*((1+i)**T)
        print("Montante Após", f"{T:.0f}","Meses: ", Capital+Va);
     case 27:                                                                                                   #Soma de Números Naturais (usando Recursão)
        print("Soma de Números Naturais (usando Recursão")
        a = int(input("Digite um Número Inteiro: "))

        def recursao(n):
             if n <=1:
              return n
             else:
              return n + recursao(n-1)
        print("Soma de Números Naturais (usando Recursão): ", recursao(a));
     case 28:                                                                                                   #Fatorial de um Número (usando Recursão)
        print("Fatorial Números Naturais (usando Recursão")
        a = int(input("Digite um Número Inteiro: "))
        print("O Fatorial de ",a, " é:", recusao1(a))
    
     case 29:                                                                                                   #Permutação
        Frase = input("Digite uma Frase/Palavra para saber quantas permutações ela possui: ")
        Frase.strip()
        esp = Frase.count(' ')
        Fra_Per = len(Frase)
        print("A Frase/Palavra:",Frase," Possui:",recusao1(Fra_Per-esp),"Formas de ser Reoganizada")
     case 30:                                                                                                   #Combinação
        n = int(input("Numero de elementos a serem cobinados (n): "))
        k = int(input("tomados de (k): "))
        Resultado = (recusao1(n)) / (recusao1(k) * recusao1(n-k))
        print(Resultado)
     case 31:                                                                                                   #Conversor de Bases Numéricas (Decimal para Binário, Hexadecimal, etc.)
        Va = int(input("Digite um valor Decimal: "))
        conversor(Va,2,'Em Binário:')
        conversor(Va,16,'Em Hexadecimal:')
     case 32:                                                                                                   #Cálculo de Média
        
        Tot_num = int(input("Quantos Números serao utilizados: "))
        media(Tot_num)
        print("A média é: ",Resultado_Media)
    
     case 33:                                                                                                   #Cálculo de Desvio Padrão
        Tot_num = int(input("Quantos Números serao utilizados: "))
        media(Tot_num)
        cont = len(cesta)
        print("A média é: ",Resultado_Media)
        while cont >0:
         print("O Desvio Padrao de", cesta[cont-1], "é: ", (Resultado_Media-cesta[cont-1]))
         cont = cont -1
     case 34:                                                                                                   #Tangente de uma Reta Dados os Coeficientes
        print("Digite os Coeficientes")
        a = float(input("A: "))
        b = float(input("B: "))
        c = float(input("C: "))
        m = -(a/b)
        RAD = math.atan(m)
        GRAU = math.degrees(RAD)
        print("O ângulo de inclinação θ é:", f"{RAD:.2f}", "radianos ou", f"{GRAU:.2f}", "graus")

if op == 1 or op ==2 or op == 3 or op == 4 or op == 5 or op ==6 or op == 7 or op == 9  :
   print("Resultado: ", Resultado )