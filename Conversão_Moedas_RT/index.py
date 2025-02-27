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
        print("-" * 25)
        op = input("Exibir Figura(S/N)?")
        if op.lower() == 's': break
        else: continue




cotacao = obter_cotacoes()
valor_normalizado = (100 / valor) * valor
montante_normalizado = (100 / valor) * mont

categorias = [moeda_destino,moeda_origem]
valores1 = [valor_normalizado, 100]  # Valor original em relação a 100
valores2 = [montante_normalizado, 100]  # Valor convertido em relação a 100

largura = 0.2  # Define largura para melhor visualização

# Criando gráfico de barras lado a lado
fig, ax = plt.subplots()
ax.bar(categorias, valores1, width=largura, color='blue', label="Valor Original", zorder=2)
ax.bar(categorias, valores2, width=largura, color='grey', label="Valor Convertido", zorder=3)
plt.ylabel('Valores ')
plt.title("Comparação de Valores ")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7, zorder=1)  # Adicionando grade

plt.show()



