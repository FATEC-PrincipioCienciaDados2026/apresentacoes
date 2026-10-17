lista_compra = []

QUANTIDADE_ITEM = 6

for contador in range(QUANTIDADE_ITEM):
    produto = input("O que voce deseja comprar? ")
    lista_compra.append(produto)

for item in lista_compra:
    print(f"Itens da lista: {item}")