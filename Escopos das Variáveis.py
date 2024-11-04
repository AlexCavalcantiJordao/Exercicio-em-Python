var_global = "Bóson Treinamentos em Tecnologia."
def escreve_texto():
    global var_global
    var_global = "Planeta Unix"
    var_local = "Alex Fonseca"
    print("Variável global: ", var_global)
    print("Variável local: ", var_local)
print("Executando a função escreve_texto: ")
escreve_texto()
print("Tentando acessar as variáveis diretamente: ")
print("Variável global: ", var_global)
