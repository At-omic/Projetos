import requests
import matplotlib.pyplot as plt

def obter_cotacoes():
    url = 'https://api.exchangerate-api.com/v4/latest/BRL'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data.get('rates',{})
    else:
        print(f"Não Foi Possivel Recuperar Dados.\n COD:{response.status_code}")
        return None

def conversor(valor, moeda_origem, moeda_destino):
    cotacao = obter_cotacoes()
    montante = valor /(cotacao[moeda_origem]/cotacao[moeda_destino])
    print(valor, cotacao[moeda_origem],cotacao[moeda_destino])
    print("-"*25)
    print(f"Valor Convertido: {montante:.2f}")
    return montante

def grafico(variavel_y_grafico,variavel_yticks_grafico,cor_traco):
    a = [1, 2]
    b = variavel_y_grafico
    x = [1, 2]
    y = [valor, mont]
    fig, ax = plt.subplots()
    plt.xticks([1, 2])
    plt.yticks(variavel_yticks_grafico)
    ax.bar(a, b, width=0.2, zorder=1, color="grey", label=f"{b[0]} U de Moedas")
    ax.scatter(x, y, zorder=2, label=f"{valor} {nome_moeda_local} -> {mont:.2f} {nome_moeda_destino}", color=f"{cor_traco}", ls=':')
    plt.plot(x,y, zorder=3, color=f"{cor_traco}")
    plt.xlabel(f"{valor}{nome_moeda_local} -> {mont:.2f}{nome_moeda_destino}")
    plt.grid(color='grey', linestyle='-', linewidth=0.1, zorder=0)
    plt.title("Relação")
    plt.legend()
    plt.show()

while True:
    try:
        print("-" * 25)
        valor = float(input("Valor a Ser convertido: "))
    except ValueError:
        print("Digite um valor Valido")
        continue

    moeda_origem = input("Sigla da Moeda de Origem: ")
    moeda_destino = input("Sigla da Moeda de Destino: ")
    if moeda_origem.upper() not in obter_cotacoes() or moeda_destino.upper() not in obter_cotacoes():
        print(f"Sigla '{moeda_origem}' ou '{moeda_destino}' Nao Encontrada!")
        continue
    else:
            mont = conversor(valor, moeda_origem.upper().strip(), moeda_destino.upper().strip())
            nome_moeda_local = moeda_origem.upper()
            nome_moeda_destino = moeda_destino.upper()
            print("-" * 25)
            if valor > mont:
                cor_traco = "red"
            else:
                cor_traco = "green"

            if valor > 100 or mont > 100:
                variavel_y_grafico = [1000,1000]
                variavel_yticks_grafico = [0,1000,valor,mont]
                grafico(variavel_y_grafico,variavel_yticks_grafico,cor_traco)
            else:
                variavel_y_grafico = [100,100]
                variavel_yticks_grafico = [0, 100,valor,mont]
                grafico(variavel_y_grafico,variavel_yticks_grafico,cor_traco)

