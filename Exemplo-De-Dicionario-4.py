dicionario = {'nome': 'Carlos', 'idade': 35, 'cidade': 'Rio de Janeiro'}

# Percorrendo as chaves
print("Chaves:")
for chave in dicionario.keys():
    print(chave)

# Percorrendo os valores
print("\nValores:")
for valor in dicionario.values():
    print(valor)

# Percorrendo chaves e valores
print("\nChaves e Valores:")
for chave, valor in dicionario.items():
    print(f'Chave: {chave}, Valor: {valor}')
