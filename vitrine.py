#Etapa 2: os dados da loja em tipos e coleções (Aula 3)

#tupla: a lista de tamanhos não muda
TAMANHOS = ("PP", "P", "M", "G", "GG")

#lista de dicionarios: um por produto
vitrine = [ 
    {"nome": "Camiseta basica", "preco": 39.90, "tamanho": "M"},
    {"nome": "Calca jeans", "preco": 129.90, "tamanho": "G"},
    {"nome": "Moletom", "preco": 159.90, "tamanho": "GG"}
]       

#Lista de pares (nome, quantidade) 
carrinho = [("Camiseta basica", 3), ("Calca jeans", 1)]

#dicionário: nome -> preço
precos = {}
for produto in vitrine:
    precos[produto["nome"]] = produto["preco"]
    
total = 0
for nome, quantidade in carrinho:
    total = total + precos[nome] * quantidade 
    
print("Peças na vitrine:", len(vitrine))
print("Total do carrinho: R$", round(total, 2))      

print(vitrine[1]["preco"])
print(TAMANHOS[-1])
print(len(carrinho))
print(precos["Moletom"] * 2)