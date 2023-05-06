import json, requests

moedas_disponiveis = ["USD", "EUR", "BRL", "JPY"]

for moeda in moedas_disponiveis:
    print(f"- {moeda}")

origem = input("Moeda de origem: ")
dest = input("Moeda de destino: ")

if origem in moedas_disponiveis and dest in moedas_disponiveis:
    requisicao = requests.get(f"https://economia.awesomeapi.com.br/{origem}-{dest}")
    cotacao = requisicao.json()

    print(f"1 {origem} equivale a {float(cotacao[0]['bid']):.2f} {dest}")
else:
    print("Moedas inválidas!")