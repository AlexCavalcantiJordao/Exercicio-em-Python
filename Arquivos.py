# Testando os métodos read(), readline() e readlines()....

manipulador = open('arquivo.txt', 'r')
print("\nMétodo read():\n")
print(manipulador.read())

manipulador.seek(0) # Volta para o inicio do arquivo....

print("\nMétodo readline():\n")
print(manipulador.readline())
print(manipulador.readline())

manipulador.seek(0)

print("\nMétodo readline():\n")
print(manipulador.readlines())

manipulador.close()

# 01

"""
print("Teste de abertura de arquivos em Python.")
print("Tentando abrir um arquivos de texto armazenado no PC:\n")

manipulador = open("arquivo.txt", "r")
for linha in manipulador:
linha = linha.rstrip()
print(linha)
manipulador.close()
"""
